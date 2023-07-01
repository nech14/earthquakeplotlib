

.PHONY: all test clean


help:
	@echo "Make project with following instructions"
    ifeq ($(OS), Windows_NT)
	    @type makefile
    else
        @cat makefile
    endif

dev:
	pip install -e .

test: dev
	pytest

build:
	pip install wheel
	python setup.py bdist_wheel

clean:
    ifeq ($(OS), Windows_NT)
	    @RMDIR /q /s "build" "dist" "vesninlib.egg-info" "vesninlib-1.0"
    else
        @rm -rf .pytest_cache/ .mypy_cache/ junit/ build/ dist/
        @find . -not -path './.venv*' -path '*/__pycache__*' -delete
        @find . -not -path './.venv*' -path '*/*.egg-info*' -delete
    endif
