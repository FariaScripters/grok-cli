# Grok CLI

This repository contains the Grok CLI, a command-line AI workflow tool that connects to your tools, understands your code and accelerates your workflows.

With the Grok CLI you can:

*   Query and edit large codebases in and beyond Grok's 1M token context window.
*   Generate new apps from PDFs or sketches, using Grok's multimodal capabilities.
*   Automate operational tasks, like querying pull requests or handling complex rebases.
*   Use tools and MCP servers to connect new capabilities, including media generation with Imagen, Veo or Lyria
*   Ground your queries with the Google Search tool, built into Grok.

## Quickstart

### Prerequisites

*   Ensure you have Python 3.9 or higher installed.
*   Install [Poetry](https://python-poetry.org/docs/#installation).

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/FariaScripters/grok-cli.git
    cd grok-cli
    ```
2.  Install the dependencies using Poetry:
    ```bash
    poetry install
    ```
3.  Activate the virtual environment:
    ```bash
    poetry shell
    ```

## Authentication

The Grok CLI requires an API key to function.

### Use a Grok API key:

1.  Generate a key from [Grok's AI Studio](https://grok.x.ai/).
2.  Set it as an environment variable in your terminal. Replace `YOUR_API_KEY` with your generated key.
    ```bash
    export GROK_API_KEY="YOUR_API_KEY"
    ```
3.  Alternatively, you can use the `login` command to save your key locally:
    ```bash
    grok login
    ```

## Usage

Once the CLI is installed and configured, you can start interacting with Grok from your shell.

### Start a conversation

```bash
grok "Write me a Grok Discord bot that answers questions using a FAQ.md file I will provide"
```

### Interactive Mode

For a continuous conversation, use the interactive flag:

```bash
grok -i
```

### Work with an existing project

Navigate to your project directory and run Grok:

```bash
cd your-project/
grok "Give me a summary of all of the changes that went in yesterday"
```

## Popular tasks

### Explore a new codebase

> Describe the main pieces of this system's architecture.
> What security mechanisms are in place?

### Work with your existing code

> Implement a first draft for GitHub issue #123.
> Help me migrate this codebase to the latest version of Java. Start with a plan.

### Automate your workflows

> Make me a slide deck showing the git history from the last 7 days, grouped by feature and team member.
> Make a full-screen web app for a wall display to show our most interacted-with GitHub issues.

### Interact with your system

> Convert all the images in this directory to png, and rename them to use dates from the exif data.
> Organize my PDF invoices by month of expenditure.

## Next steps

*   Learn how to [contribute to or build from the source](CONTRIBUTING.md).
*   Explore the available [CLI Commands](docs/commands.md).
*   If you encounter any issues, review the [troubleshooting guide](docs/troubleshooting.md).

## Troubleshooting

If you're having issues, please refer to the [troubleshooting guide](docs/troubleshooting.md).

## Uninstall

To uninstall the Grok CLI, remove the project directory and the virtual environment created by Poetry.

## Terms of Service and Privacy Notice

For details on the terms of service and privacy notice applicable to your use of Grok CLI, see the [Terms of Service](TERMS.md) and [Privacy Notice](PRIVACY.md).
