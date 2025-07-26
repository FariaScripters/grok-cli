# CLI Commands

The Grok CLI provides a set of commands to interact with the Grok API and manage your workflows.

## Main Commands

### `grok [message]`

This is the primary command for interacting with Grok. You can pass a message directly to the CLI.

**Options:**

*   `--model, -m`: Specify the model to use (e.g., `grok-1`).
*   `--interactive, -i`: Enable interactive chat mode.

### `grok login`

Authenticates the CLI with your Grok API key. It will prompt you to enter your key, which will be stored securely on your local machine.

### `grok config`

Allows you to manage the CLI configuration.

**Subcommands:**

*   `grok config get <key>`: Get a configuration value.
*   `grok config set <key> <value>`: Set a configuration value.
*   `grok config delete <key>`: Delete a configuration value.

## Planned Commands

The following commands are planned for future releases:

*   `grok analyze`: Analyze a codebase.
*   `grok prototype`: Generate an application from a PDF or sketch.
*   `grok devops`: Perform DevOps tasks.
*   `grok media`: Generate media.
*   `grok search`: Perform a web search.
