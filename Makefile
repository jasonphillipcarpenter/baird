
.PHONY: install test

default: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=./:./tests poetry run pytest --cov=baird --disable-warnings

coverage:
	poetry run pytest --cov-report html:cov_html \
		--cov-branch \
		--cov=baird tests/

