import os
from pathlib import Path
from typing import Dict, Optional
import json

CONFIG_DIR = Path.home() / ".config" / "grok-cli"
CONFIG_FILE = CONFIG_DIR / "config.json"

class Config:
    """Configuration manager for grok-cli."""
    def __init__(self):
        self.config: Dict = {}
        self._load_config()

    def _load_config(self):
        """Load configuration from file."""
        if CONFIG_FILE.exists():
            try:
                self.config = json.loads(CONFIG_FILE.read_text())
            except json.JSONDecodeError:
                self.config = {}

    def _save_config(self):
        """Save configuration to file."""
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        CONFIG_FILE.write_text(json.dumps(self.config, indent=2))

    def get(self, key: str, default: Optional[str] = None) -> Optional[str]:
        """Get a configuration value."""
        return self.config.get(key) or os.environ.get(key) or default

    def set(self, key: str, value: str):
        """Set a configuration value."""
        self.config[key] = value
        self._save_config()

    def delete(self, key: str):
        """Delete a configuration value."""
        if key in self.config:
            del self.config[key]
            self._save_config()
