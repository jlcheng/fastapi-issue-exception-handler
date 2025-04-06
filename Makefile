run:
	uv run src/main.py

test:
	uv run pytest tests

check:
	uvx ruff check
	uv run mypy src tests

fmt:
	uvx ruff format
	uvx ruff check --fix

