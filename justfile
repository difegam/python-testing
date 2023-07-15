set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]
# set dotenv-load := true

alias i := install
alias t := test
alias pcheck := pre-commit-check

# Available recipes
_default:
    @just --list --unsorted --list-prefix "    > " --justfile {{justfile()}}

# Init project
init:
    poetry-install

# Run tests
test:
    @echo "Testing app...!\n"
    poetry run pytest tests/

# Manually run all pre-commit hooks on repository
pre-commit-check:
    pre-commit run --all-files

install:
    pip install pre-commit

requirements env="PRD":
    poetry export -f requirements.txt -o requirements.txt --without-hashes {{ if env == "DEV" { "--dev" } else {" "} }}

# Install Poetry - Linux & macOS
[unix]
poetry-install:
    curl -sSL https://install.python-poetry.org | python3 -

# Install Poetry - Windows (Powershell)
[windows]
poetry-install:
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# Just Programmer's Manual
[windows]
@help command="just":
    start {{ if command == "just" { "https://just.systems/man/en/" } else if command == "poetry" { "https://python-poetry.org/docs/" } else { "https://www.google.com/" } }}
    echo "help - {{command}}"
# Just Programmer's Manual
[unix]
@help:
    start https://just.systems/man/en/
