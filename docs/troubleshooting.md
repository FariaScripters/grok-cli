# Troubleshooting Guide

If you encounter issues while using the Grok CLI, this guide may help you resolve them.

## Common Issues

### `Command not found: grok`

This error usually means that the shell can't find the `grok` executable.

**Solution:**

1.  Make sure you have activated the Poetry virtual environment:
    ```bash
    poetry shell
    ```
2.  If you are still having issues, you can run the CLI directly with `poetry run`:
    ```bash
    poetry run grok "your message"
    ```

### API Key Not Found

If you see an error message about a missing API key, it means the CLI can't find your Grok API key.

**Solution:**

1.  Ensure you have set the `GROK_API_KEY` environment variable correctly.
    ```bash
    export GROK_API_KEY="YOUR_API_KEY"
    ```
2.  Alternatively, run `grok login` to store your API key locally.

### Installation Issues

If you have problems installing the dependencies with `poetry install`, it could be due to a corrupted cache or network issues.

**Solution:**

1.  Clear Poetry's cache:
    ```bash
    poetry cache clear --all .
    ```
2.  Try installing again.

## Getting Help

If you're still having trouble, please [open an issue](https://github.com/FariaScripters/grok-cli/issues) on our GitHub repository.
