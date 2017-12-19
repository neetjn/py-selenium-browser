setup:
	virtualenv venv
	venv/bin/pip install -r tests/test-requirements.txt

test:
# run e2e tests
	venv/bin/pytest --cov=pysbr tests/test_*.py

package:
	python setup.py sdist

publish: package
	twine upload dist/*
