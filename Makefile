test:
	python test_simpleeval.py

clean:
	rm -rf build
	rm -rf dist

build:
	python setup.py sdist build

upload:
	python setup.py sdist upload -r $(repository)

.PHONY: test clean build upload
