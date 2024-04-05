#!/usr/bin/env make
.DEFAULT_GOAL := test

.PHONY: check
## Code style checking and linting
check:
	@echo Code style checking and linting
	python -m isort setup.py src/ tests/

	@echo Format code. Manage indents, break lines exceeding max line lengths
	python -m black -l  80 -t py38 -q src/ tests/

	@echo Check code for
	python -m flake8 --docstring-convention=google src/ tests/

	@echo Running static checker
	mypy src/ tests/

.PHONY: check-notebook
check-notebook:
	@echo Code style checking and linting
	nbqa isort notebooks

	@echo Format code. Manage indents, break lines exceeding max line lengths
	nbqa black --line-length=80 notebooks

	@echo Check code for
	nbqa flake8 --docstring-convention=google notebooks

	@echo Running static checker
	nbqa mypy notebooks


.PHONY: test
## Pytest validation
test:
	@echo Testing code: Running pytest
	@python -m pytest --ff --cov=src/ --cov-report=term-missing tests/


.PHONY: clean
## Cleanup generated files
clean:
	-rm -r .pytest_cache
	-rm -f .coverage
	-rm -r build/ dist/ *.egg-info
	-find . -type d -name __pycache__ -exec rm -rf "{}" \;
