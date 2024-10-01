
.PHONY: install build test coverage

default: test

install:
	pipenv install --dev --skip-lock

build:
	poetry build

test:
	PYTHONPATH=./:./tests poetry run pytest --cov=baird --disable-warnings

coverage:
	poetry run pytest --cov-report html:cov_html \
		--cov-branch \
		--cov=baird tests/

