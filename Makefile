
# local dev

test:
	PYTHONPATH=src pytest -c pytest.ini


# docker commands

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

restart:
	docker-compose restart

logs:
	docker-compose logs -f


# hopeiq

info:
	docker exec -it hopeiq_rpc hopeiq info

bootstrap:
	docker exec -it hopeiq_rpc hopeiq sync-config
	docker exec -it hopeiq_rpc hopeiq bootstrap --wipe

nlp_example:
	docker exec -it hopeiq_rpc python -m ignitenlp.cli /data/example.pdf /data/example.json

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

.PHONY: build test
