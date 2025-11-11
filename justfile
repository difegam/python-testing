set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]
set dotenv-load := true

alias i := install
alias t := test
alias l := lint
alias c := check

# Available recipes
@_:
    just --list

# Ensure project virtualenv is up to date
[group("development")]
install:
    @echo "📦 Installing the application for development"
    uv sync --all-groups
    uv run pre-commit install
    @echo "\n✅ Setup complete, ready to code 🚀"

# Run linter and formatter
[group("qa")]
lint:
    uv run ruff check --unsafe-fixes
    uv run ruff format

# Run pre-commit hooks on all files
[group('qa')]
check:
    @echo "Running pre-commit hooks on all files"
    @uv run pre-commit run --all-files

# Run tests
[group('testing')]
test:
    @echo "Testing app...!\n"
    uv run pytest tests/

# Install Poetry - Linux & macOS
[group("installation")]
[unix]
uv-install:
    # On macOS and Linux.
    curl -LsSf https://astral.sh/uv/install.sh | sh

# Install Poetry - Windows (Powershell)
[group("installation")]
[windows]
uv-install:
    # On Windows.
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
