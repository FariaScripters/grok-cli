"""Main entry point for the Grok CLI application."""
import typer
from rich.console import Console

from .commands.chat import app as chat_app
from .auth.login import login, logout

app = typer.Typer(
    help="An open-source AI agent that brings the power of Grok directly into your terminal",
    rich_markup_mode="rich",
)

# Add subcommands
app.command()(login)
app.command()(logout)
app.add_typer(chat_app, name="chat", help="Chat with Grok AI")
config = Config()

def setup_client() -> AsyncOpenAI:
    """Set up the OpenAI client with retry logic."""
    api_key = config.get("XAI_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/bold red] XAI_API_KEY not set. Run 'grok config set XAI_API_KEY your-key'")
        raise typer.Exit(1)

    return AsyncOpenAI(
        api_key=api_key,
        base_url="https://api.x.ai/v1",
    )

@backoff.on_exception(
    backoff.expo,
    Exception,
    max_tries=3,
    max_time=30,
)
async def chat_with_grok(
    client: AsyncOpenAI,
    messages: List[dict],
    model: str = "grok-2-latest",
) -> ChatCompletion:
    """Send messages to Grok and get the response with retry logic."""
    try:
        return await client.chat.completions.create(
            model=model,
            messages=messages,
        )
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        raise

def format_response(response: str) -> None:
    """Format and print the response with syntax highlighting for code blocks."""
    # Split on code blocks
    parts = response.split("```")
    
    for i, part in enumerate(parts):
        if i % 2 == 0:  # Regular text
            if part.strip():
                console.print(Markdown(part))
        else:  # Code block
            lang = part.split('\n')[0] if '\n' in part else ''
            code = '\n'.join(part.split('\n')[1:]) if '\n' in part else part
            if code.strip():
                syntax = Syntax(code, lang or "python", theme="monokai", line_numbers=True)
                console.print(Panel(syntax, border_style="blue"))

@app.command()
def analyze(directory: str):
    """Analyze a large codebase."""
    typer.echo(f"Analyzing codebase at {directory}... (TBD)")

@app.command()
def prototype(input_file: str):
    """Generate an app prototype from a PDF or sketch."""
    typer.echo(f"Generating prototype from {input_file}... (TBD)")

@app.command()
def devops(task: str, repo: str = None):
    """Perform DevOps tasks like fetching PRs."""
    typer.echo(f"Performing DevOps task: {task} for repo: {repo or 'local'}... (TBD)")

@app.command()
def media(model: str, prompt: str):
    """Generate media using models like Imagen."""
    typer.echo(f"Generating media with {model} and prompt '{prompt}'... (TBD)")

@app.command()
def search(query: str):
    """Perform a web search."""
    typer.echo(f"Searching for '{query}'... (TBD)")


@app.command()
def chat(
    message: Optional[str] = typer.Argument(None, help="Message to send to Grok"),
    model: str = typer.Option("grok-2-latest", help="Model to use for chat completion"),
    system: str = typer.Option(
        "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.",
        help="System message for chat context",
    ),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Start an interactive chat session"),
    stream: bool = typer.Option(False, "--stream", "-s", help="Stream the response as it's generated"),
):
    """Chat with Grok AI."""
    client = setup_client()
    messages = [{"role": "system", "content": system}]

    async def process_message(msg: str) -> None:
        messages.append({"role": "user", "content": msg})
        
        if stream:
            response_text = ""
            async for chunk in await client.chat.completions.create(
                model=model,
                messages=messages,
                stream=True,
            ):
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    console.print(content, end="")
                    response_text += content
            console.print()  # New line after streaming
            messages.append({"role": "assistant", "content": response_text})
        else:
            with console.status("[bold yellow]Grok is thinking...[/bold yellow]", spinner="dots"):
                completion = await chat_with_grok(client, messages, model)
                response = completion.choices[0].message.content
                messages.append({"role": "assistant", "content": response})
                format_response(response)

    if interactive:
        console.print("[bold blue]Starting interactive chat with Grok. Type 'exit' to quit.[/bold blue]")
        while True:
            try:
                user_input = Prompt.ask("\n[bold green]You[/bold green]")
                if user_input.lower() == "exit":
                    break
                asyncio.run(process_message(user_input))
            except KeyboardInterrupt:
                console.print("\n[bold yellow]Chat session ended.[/bold yellow]")
                break
            except Exception as e:
                console.print(f"\n[bold red]Error:[/bold red] {str(e)}")
                continue
    elif message:
        asyncio.run(process_message(message))
    else:
        console.print("[bold red]Error:[/bold red] Please provide a message or use --interactive mode")
        raise typer.Exit(1)

@app.command()
def config(
    action: str = typer.Argument(..., help="Action to perform: get, set, delete"),
    key: str = typer.Argument(..., help="Configuration key"),
    value: Optional[str] = typer.Argument(None, help="Configuration value (for set action)"),
):
    """Manage configuration settings."""
    if action == "get":
        value = config.get(key)
        if value:
            console.print(f"{key}={value}")
        else:
            console.print(f"[yellow]No value set for {key}[/yellow]")
    elif action == "set":
        if not value:
            value = Prompt.ask(f"Enter value for {key}", password=True)
        config.set(key, value)
        console.print(f"[green]Set {key}[/green]")
    elif action == "delete":
        config.delete(key)
        console.print(f"[yellow]Deleted {key}[/yellow]")
    else:
        console.print("[red]Invalid action. Use: get, set, or delete[/red]")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
