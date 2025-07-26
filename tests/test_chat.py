"""Tests for the chat functionality."""
from unittest.mock import AsyncMock, patch
import pytest
from grok_cli.commands.chat import async_chat

@pytest.mark.asyncio
async def test_async_chat():
    """Test the async chat functionality."""
    mock_response = AsyncMock()
    mock_response.choices = [AsyncMock(message=AsyncMock(content="Test response"))]
    
    with patch("openai.AsyncOpenAI") as mock_client:
        mock_client.return_value.chat.completions.create = AsyncMock(return_value=mock_response)
        
        await async_chat(
            message="test message",
            model="test-model",
            temperature=0.7,
            api_key="test-key"
        )
