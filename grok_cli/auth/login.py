"""Authentication module for Grok CLI."""
from typing import Optional
import os
import json
from pathlib import Path
import typer
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def get_config_dir() -> Path:
    """Get the configuration directory for storing credentials."""
    config_dir = Path.home() / ".config" / "grok-cli"
    config_dir.mkdir(parents=True, exist_ok=True)
    return config_dir

def save_credentials(api_key: str) -> None:
    """Save API credentials securely."""
    config_file = get_config_dir() / "credentials.json"
    with open(config_file, "w") as f:
        json.dump({"api_key": api_key}, f)
    os.chmod(config_file, 0o600)  # Set file permissions to user read/write only

def get_credentials() -> Optional[str]:
    """Get stored API credentials."""
    config_file = get_config_dir() / "credentials.json"
    if not config_file.exists():
        return None
    
    with open(config_file) as f:
        try:
            creds = json.load(f)
            return creds.get("api_key")
        except json.JSONDecodeError:
            return None

def login() -> None:
    """Interactive login command."""
    api_key = Prompt.ask("Enter your Grok API key", password=True)
    save_credentials(api_key)
    console.print("[green]Successfully saved credentials![/green]")

def logout() -> None:
    """Remove stored credentials."""
    config_file = get_config_dir() / "credentials.json"
    if config_file.exists():
        config_file.unlink()
    console.print("[yellow]Logged out successfully[/yellow]")
