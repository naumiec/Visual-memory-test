.PHONY: venv install install-novenv install-novenv3 run run-novenv run-novenv3 convert experiment clean docs help

VENV_DIR := venv
PYTHON := $(VENV_DIR)/bin/python3
PYTHON_3_8 := python3.8
PIP := $(VENV_DIR)/bin/pip3
DOXYGEN := doxygen
DOXYFILE := Doxyfile

UNAME_S := $(shell uname -s)
ifeq ($(UNAME_S), Linux)
	OS_TYPE := Linux
else ifeq ($(UNAME_S), Darwin)
	OS_TYPE := macOS
else
	OS_TYPE := Windows
	VENV_DIR := venv/Scripts
	PYTHON := $(VENV_DIR)/python.exe
	PIP := $(VENV_DIR)/pip.exe
endif

venv:
	python3 -m venv $(VENV_DIR)

install: venv
	$(PIP) install -r requirements.txt

install-novenv:
	$(PYTHON_3_8) -m pip install -r requirements.txt

run: venv
	$(PYTHON) ./src/main.py

run-novenv:
	$(PYTHON_3_8) ./src/main.py

clean:
	rm -rf $(VENV_DIR) ./results/*.csv ./results/*.txt ./results/*.json ./plots/*.png
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

docs:
	$(DOXYGEN) $(DOXYFILE)

help:
	@echo "Makefile for Visual Memory Test Project"
	@echo ""
	@echo "Detected OS: $(OS_TYPE)"
	@echo ""
	@echo "Usage:"
	@echo "  make venv              - Create a virtual environment"
	@echo "  make install           - Install dependencies"
	@echo "  make install-novenv    - Install dependencies with Python 3.8 without virtual environment"
	@echo "  make run               - Run the main script"
	@echo "  make run-novenv        - Run the main script with Python 3.8 without virtual environment"
	@echo "  make clean             - Clean the environment"
	@echo "  make help              - Display this help message"
	@echo "  make docs              - Generate documentation"
	@echo ""
