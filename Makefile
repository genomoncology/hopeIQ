# local dev

test:
	pytest -c pytest.ini


# clean

clean: clean-build clean-pyc clean-test clean-uploads

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	find . -name 'htmlcov' -exec rm -fr {} +
	find . -name '.coverage' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +
	find . -name '.cache' -exec rm -fr {} +
	find . -name '.mypy_cache' -exec rm -fr {} +

clean-uploads:
	rm -fr examples/uploads/*
