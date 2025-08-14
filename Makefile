.PHONY: test test-verbose test-cov install dev clean help

# Default target
help:
	@echo "Zari Agent - Available commands:"
	@echo "  make test        - Run all tests"
	@echo "  make test-verbose - Run tests with verbose output"
	@echo "  make test-cov    - Run tests with coverage report"
	@echo "  make install     - Install dependencies"
	@echo "  make dev         - Install development dependencies"
	@echo "  make clean       - Clean cache and temporary files"

# Install dependencies
install:
	uv install

# Install development dependencies
dev:
	uv add pytest pytest-cov --optional test

# Run tests
test:
	uv run python test.py

# Run tests with verbose output
test-verbose:
	uv run pytest tests.py --verbose

# Run tests with coverage
test-cov:
	uv run pytest tests.py --cov=functions --cov-report=term-missing --cov-report=html

# Clean cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
