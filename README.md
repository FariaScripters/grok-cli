# Grok CLI

An open-source AI agent that brings the power of Grok directly into your terminal.

## Installation

1. Make sure you have Python 3.9 or later installed
2. Install Poetry (package manager):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/FariaScripters/grok-cli.git
   cd grok-cli
   ```
4. Install dependencies:
   ```bash
   poetry install
   ```

## Configuration

Set your X.AI API key as an environment variable:
```bash
export XAI_API_KEY="your-api-key-here"
```

## Usage

### Single Message Mode
```bash
grok "What is the meaning of life?"
```

### Interactive Chat Mode
```bash
grok --interactive
# or
grok -i
```

### Specify Different Model
```bash
grok "Hello" --model "grok-1"
```

## Features

- 🚀 Simple and intuitive CLI interface
- 💬 Interactive chat mode
- 🎨 Rich terminal output with colors and spinners
- ⚡ Async API calls for better performance
- 🔒 Secure API key management

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
