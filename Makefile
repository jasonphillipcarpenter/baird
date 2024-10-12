.PHONY: default
default: test

.PHONY: install
install:
	pip install -e .

.PHONY: install_pkgs
install_pkgs:
	poetry install --dev --skip-lock

.PHONY: build
build:
	poetry build

.PHONY: test
test:
	PYTHONPATH=./:./tests poetry run pytest --cov=baird --disable-warnings

.PHONY: coverage
coverage:
	poetry run pytest --cov-report html:cov_html \
		--cov-branch \
		--cov=baird tests/
