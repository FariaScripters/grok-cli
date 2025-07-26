"""Tests for the configuration module."""
import pytest
from pathlib import Path
from grok_cli.config import Config

def test_config_get_set():
    """Test getting and setting configuration values."""
    config = Config()
    config.set("test_key", "test_value")
    assert config.get("test_key") == "test_value"

def test_config_delete():
    """Test deleting configuration values."""
    config = Config()
    config.set("test_key", "test_value")
    config.delete("test_key")
    assert config.get("test_key") is None

def test_config_environment_variable(monkeypatch):
    """Test that environment variables take precedence."""
    monkeypatch.setenv("TEST_ENV_KEY", "env_value")
    config = Config()
    config.set("TEST_ENV_KEY", "config_value")
    assert config.get("TEST_ENV_KEY") == "env_value"
