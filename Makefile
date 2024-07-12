install:
	poetry install

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 hexlet_code

gendiff:
	poetry run gendiff -h

test:
	poetry run pytest

tests-coverage:
	poetry run pytest --cov=hexlet_code --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint
