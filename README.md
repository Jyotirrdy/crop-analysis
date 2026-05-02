# Crop Analysis Project

This repository now contains a simple Python project for analyzing crop production datasets.

## Features
- Load crop records from CSV
- Compute overall and per-crop average yield (tons/hectare)
- Identify best-performing crop
- Generate a basic rainfall-to-yield trend hint
- Run analysis via CLI

## Project structure
- `src/crop_analysis/analyzer.py`: core data model and analysis logic
- `src/crop_analysis/cli.py`: command-line interface
- `data/sample_crop_data.csv`: sample input dataset
- `tests/test_analyzer.py`: basic unit tests

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
crop-analysis data/sample_crop_data.csv
```

## Run tests
```bash
PYTHONPATH=src python -m unittest discover -s tests -p 'test_*.py'
```
