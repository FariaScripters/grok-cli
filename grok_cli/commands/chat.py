"""Command implementations for Grok CLI."""
import typer
from rich.console import Console
from rich.markdown import Markdown
from openai import AsyncOpenAI
import asyncio
import backoff

from ..config import Config
from ..models import list_available_models, DEFAULT_MODEL

app = typer.Typer()
console = Console()
config = Config()

@app.command()
def chat(
    message: str = typer.Argument(..., help="Message to send to Grok"),
    model: str = typer.Option(DEFAULT_MODEL, help="Model version to use. Available models: " + ", ".join(list_available_models())),
    temperature: float = typer.Option(0.7, help="Temperature for response generation"),
):
    """Start a chat with Grok."""
    api_key = config.get("XAI_API_KEY")
    if not api_key:
        console.print("[red]Please login first using 'grok login'[/red]")
        raise typer.Exit(1)
    
    asyncio.run(async_chat(message, model, temperature, api_key))

@backoff.on_exception(backoff.expo, Exception, max_tries=3)
async def async_chat(message: str, model: str, temperature: float, api_key: str):
    """Async chat implementation with retry logic."""
    client = AsyncOpenAI(api_key=api_key)
    
    try:
        with console.status("[bold green]Thinking..."):
            response = await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": message}],
                temperature=temperature,
            )
        
        content = response.choices[0].message.content
        if content:
            console.print(Markdown(content))
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
