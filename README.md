# Zari Agent

A Python-based AI coding agent powered by Google's Gemini AI that can perform file operations, execute code, and provide intelligent assistance for software development tasks.

## Features

- **File Operations**: List directories, read file contents, and write files
- **Code Execution**: Run Python scripts with arguments
- **AI-Powered Analysis**: Explain code, debug issues, and provide detailed project overviews
- **Multi-step Reasoning**: Performs complex tasks through multiple function calls
- **Safety Constraints**: Operations are restricted to designated working directories

## Project Structure

```
zari-agent/
├── main.py              # Main entry point for the AI agent
├── config.py            # Configuration and system prompts
├── test.py              # Test runner script
├── Makefile             # Build and test commands
├── .env.example         # Environment variables template
├── functions/           # Available functions for the AI agent
│   ├── functions.py     # Function registry and dispatcher
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── calculator/          # Example project for testing
│   ├── main.py
│   ├── tests.py
│   └── pkg/
│       ├── calculator.py
│       └── render.py
└── tests.py            # Main test suite
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/zari-agent.git
   cd zari-agent
   ```

2. **Install dependencies** (using uv):
   ```bash
   uv install
   ```

   Or with pip (after installing uv dependencies):
   ```bash
   pip install google-genai python-dotenv
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your Google Gemini API key.

## Configuration

Create a `.env` file with the following variables:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

To get a Gemini API key:
1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Create a new API key
3. Copy the key to your `.env` file

## Usage

### Basic Usage

```bash
uv run main.py "your prompt here"
```

### Examples

**Explain code files:**
```bash
uv run main.py "Explain all the Python code files in this project"
```

**Debug issues:**
```bash
uv run main.py "explain the bug in calculator: 3 + 7 * 2 shouldn't be 20"
```

**Run tests:**
```bash
uv run main.py "run tests.py"
```

**Get project overview:**
```bash
uv run main.py "Provide a summary of what each file does and how they work together"
```

### Verbose Mode

Add `--verbose` to see detailed information about function calls and token usage:

```bash
uv run main.py "your prompt here" --verbose
```

## Available Functions

The AI agent has access to these functions:

- **get_files_info**: List files and directories with size information
- **get_file_content**: Read the contents of files (with character limits)
- **write_file**: Create or modify files
- **run_python_file**: Execute Python scripts with optional arguments

## System Behavior

- **Read-only by default**: When asked to "explain" issues, the agent only provides analysis without making changes
- **Explicit actions**: The agent only modifies files when explicitly asked to fix or write something
- **Safety first**: All file operations are constrained to the working directory
- **Smart prioritization**: Focuses on code files over placeholder files when analyzing projects

## Development

### Running Tests

You can run tests in several ways:

**Using the test script (recommended):**
```bash
uv run test.py
```

**Using pytest directly:**
```bash
uv run pytest tests.py
```

**Using Make (if you have make installed):**
```bash
make test          # Run all tests
make test-verbose  # Run with verbose output
make test-cov      # Run with coverage report
```

**Install test dependencies:**
```bash
uv add pytest pytest-cov --optional test
```

Or if using pip:
```bash
pip install pytest pytest-cov
```

### Testing the Calculator Example

```bash
uv run calculator/main.py "3 + 7 * 2"
```

### Quick Commands

```bash
# Run tests
uv run test.py

# Run with coverage
uv run pytest tests.py --cov=functions

# Clean cache files  
make clean

# Install all dependencies
make install && make dev
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Dependencies

- **google-genai**: Google's Gemini AI client library
- **python-dotenv**: Environment variable management

## Requirements

- Python 3.13+
- Google Gemini API key