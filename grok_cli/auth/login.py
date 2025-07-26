"""Authentication module for Grok CLI."""
from rich.console import Console
from rich.prompt import Prompt
from ..config import Config

console = Console()
config = Config()

def login() -> None:
    """Interactive login command."""
    api_key = Prompt.ask("Enter your XAI API key", password=True)
    config.set("XAI_API_KEY", api_key)
    console.print("[green]Successfully saved API key![/green]")

def logout() -> None:
    """Remove stored credentials."""
    config.delete("XAI_API_KEY")
    console.print("[yellow]Logged out successfully[/yellow]")
