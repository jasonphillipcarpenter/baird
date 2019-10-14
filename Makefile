
.PHONY: install test

default: test

install:
	pipenv install --dev --skip-lock

test:
	PYTHONPATH=./src:./tests pytest --cov=src/baird

coverage:
	pytest --cov-report html:cov_html \
		--cov-branch \
		--cov=src/baird tests/

