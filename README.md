# Visual Memory Test

## Overview

This repository contains the implementation of a Visual Memory Test designed to assess the working memory capacity of individuals by requiring them to memorize and recall the positions of highlighted squares on a grid. The project includes Python scripts to run the experiment, record results, and provide instructions to participants.

## Table of contents

1. [Introduction](#introduction)
2. [Procedure](#procedure)
3. [Stimuli and presentation](#stimuli-and-presentation)
4. [Colors used](#colors-used)
5. [Result logging](#result-logging)
6. [Getting started](#getting-started)
7. [Files in the repository](#files-in-the-repository)
8. [Makefile commands](#makefile-commands)
9. [References](#references)

## Introduction

Visual Memory Tests are diagnostic tools used in psychology and neuropsychology to assess an individual's ability to remember and reproduce visual information. This particular test evaluates how well a person can remember the positions of highlighted squares on a grid, reflecting their working memory capacity.

## Procedure

The Visual Memory Test consists of multiple stages, each involving the following steps:

1. A grid with highlighted squares is displayed for 2 seconds.
2. A new grid, identical to the first but without highlighted squares, is shown. The participant must recall and click on the positions of the previously highlighted squares.
3. Correct clicks reveal the highlighted squares again. Incorrect clicks cause the square to disappear, and it cannot be clicked again.
4. The test progresses through stages with an increasing number of highlighted squares. The initial grid size is 3x3 with 3 highlighted squares, expanding as the test progresses.
5. The test ends after 20 stages, 3 errors within a stage, or the participant completes all 4 rounds (1 training and 3 testing rounds).

## Stimuli and presentation

- The test window occupies the full screen to minimize distractions.
- The grid has a 1:1 width-to-height ratio and is divided into equal-sized square sections.
- Highlighted squares are a different color from the others, with distinguishable colors used for accessibility.
- Instructions and transitional screens are centrally displayed in a readable font.

## Colors used

- Background: Dark gray (e.g., RGB #1A0A1A)
- Regular squares: Dark but distinguishable (e.g., blue, RGB #0000FF)
- Highlighted squares: Bright and easily distinguishable (e.g., yellow, RGB #FFFF00)
- Transitional screen text: Bright and close to white (e.g., RGB #FAFAF6)

## Result logging

Results are automatically saved to a text file after the test completes. The filename is based on the date and time of the test (format: YYYYMMDDhhmm). The file includes:

- Session and stage numbers
- Positions of highlighted squares in each stage
- Time spent memorizing and clicking
- Positions clicked by the participant

The data is formatted for easy import into spreadsheet software (e.g., Excel, CSV).

## Getting started

### Using Makefile

1. **Clone the repository**:
   ```sh
   git clone https://github.com/naumiec/visual-memory-test.git
   cd visual-memory-test
   ```
2. **Create a virtual environment and install dependencies**:
   ```sh
   make venv
   make install
   ```
3. **Run the experiment**:
   ```sh
   make run
   ```

### Using Python directly

1. **Clone the repository**:
   ```sh
   git clone https://github.com/naumiec/visual-memory-test.git
   cd visual-memory-test
   ```
2. **Create a virtual environment**:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
   Depending on your system, you might need to use `python` instead of `python3`:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install the required packages**:
   ```sh
   pip3 install -r requirements.txt
   ```
   Depending on your system, you might need to use `pip` instead of `pip3`:
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the experiment**:
   ```sh
   python3 src/main.py 
   ```
   Depending on your system, you might need to use `python` instead of `python3`:
   ```sh
   python src/main.py 
   ```

## Files in the repository

- `Makefile`: Instructions for setting up and running the project.
- `src/main.py`: Entry point for the application.
- `src/Experiment.py`: Core script for running the visual memory test.
- `src/Converter.py`: Script for converting data formats.
- `src/Colors.py`: Script for defining colors used in the test.
- `src/Plotter.py`: Script for plotting test results.
- `results/`: Directory for storing test results (file formats: `.txt`, `.csv`, `.json`).
- `plots/`: Directory for storing plots of test results (file format: `.png`).
- `test_procedure_specification.pdf`: Detailed specification of the experimental procedure.
- `requirements.txt`: List of Python packages required for the project.
- `README.md`: Project overview and instructions.
- `Doxyfile`: Configuration file for generating documentation using Doxygen.
- `documentation.pdf`: Documentation generated using Doxygen.

## Makefile commands

- `make help`: Show available commands.
- `make venv`: Create a virtual environment.
- `make install`: Install dependencies in the virtual environment.
- `make install-novenv`: Install dependencies globally with Python 3.8.
- `make run`: Run the visual memory test in the virtual environment.
- `make run-novenv`: Run the visual memory test globally with Python 3.8.
- `make clean`: Remove the virtual environment and temporary files.
- `make docs`: Generate documentation using Doxygen.

## References

Ashford, J. W. (2005). Memtrax computerized memory test, a one-minute dementia screen. *Alzheimers Dementia, 1(1), S23*. [Link to paper](https://alz-journals.onlinelibrary.wiley.com/doi/10.1016/j.jalz.2005.06.111)
