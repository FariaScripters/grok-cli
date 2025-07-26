import os
import asyncio
from typing import Optional
import typer
from openai import AsyncOpenAI
from rich.console import Console
from rich.prompt import Prompt
from rich import print as rprint

app = typer.Typer(help="An open-source AI agent that brings the power of Grok directly into your terminal")
console = Console()

async def chat_with_grok(
    client: AsyncOpenAI,
    message: str,
    model: str = "grok-2-latest",
    system_message: str = "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy.",
) -> str:
    """Send a message to Grok and get the response."""
    try:
        completion = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": message},
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        raise typer.Exit(1)

@app.command()
def chat(
    message: Optional[str] = typer.Argument(None, help="Message to send to Grok"),
    model: str = typer.Option("grok-2-latest", help="Model to use for chat completion"),
    interactive: bool = typer.Option(False, "--interactive", "-i", help="Start an interactive chat session"),
):
    """Chat with Grok AI."""
    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/bold red] XAI_API_KEY environment variable is not set")
        raise typer.Exit(1)

    client = AsyncOpenAI(
        api_key=api_key,
        base_url="https://api.x.ai/v1",
    )

    if interactive:
        console.print("[bold blue]Starting interactive chat with Grok. Type 'exit' to quit.[/bold blue]")
        while True:
            try:
                user_input = Prompt.ask("\n[bold green]You[/bold green]")
                if user_input.lower() == "exit":
                    break
                
                with console.status("[bold yellow]Grok is thinking...[/bold yellow]", spinner="dots"):
                    response = asyncio.run(chat_with_grok(client, user_input, model))
                console.print(f"\n[bold blue]Grok:[/bold blue] {response}")
            except KeyboardInterrupt:
                console.print("\n[bold yellow]Chat session ended.[/bold yellow]")
                break
            except Exception as e:
                console.print(f"\n[bold red]Error:[/bold red] {str(e)}")
                continue
    
    elif message:
        with console.status("[bold yellow]Grok is thinking...[/bold yellow]", spinner="dots"):
            response = asyncio.run(chat_with_grok(client, message, model))
        console.print(f"\n[bold blue]Grok:[/bold blue] {response}")
    else:
        console.print("[bold red]Error:[/bold red] Please provide a message or use --interactive mode")
        raise typer.Exit(1)
        console.print("[bold blue]Starting interactive chat with Grok. Type 'exit' to quit.[/bold blue]")
        while True:
            message = Prompt.ask("\n[bold green]You[/bold green]")
            if message.lower() == "exit":
                break
            
            with console.status("[bold yellow]Grok is thinking...[/bold yellow]", spinner="dots"):
                response = asyncio.run(chat_with_grok(client, message, model))
            console.print(f"\n[bold blue]Grok:[/bold blue] {response}")
    
    elif message:
        with console.status("[bold yellow]Grok is thinking...[/bold yellow]", spinner="dots"):
            response = asyncio.run(chat_with_grok(client, message, model))
        console.print(f"\n[bold blue]Grok:[/bold blue] {response}")
    else:
        console.print("[bold red]Error:[/bold red] Please provide a message or use --interactive mode")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
        console.print("[bold green]Starting interactive chat session with Grok. Type 'exit' to quit.[/bold green]")
        while True:
            message = Prompt.ask("\n[bold blue]You[/bold blue]")
            if message.lower() in ("exit", "quit"):
                break

            with console.status("[bold yellow]Grok is thinking...", spinner="dots"):
                response = asyncio.run(chat_with_grok(client, message, model))
            
            console.print(f"\n[bold green]Grok:[/bold green] {response}")
    else:
        if not message:
            console.print("[bold red]Error:[/bold red] Please provide a message or use --interactive mode")
            raise typer.Exit(1)

        with console.status("[bold yellow]Grok is thinking...", spinner="dots"):
            response = asyncio.run(chat_with_grok(client, message, model))
        
        console.print(f"\n[bold green]Grok:[/bold green] {response}")

if __name__ == "__main__":
    app()
