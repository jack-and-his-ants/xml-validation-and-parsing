![Python](https://img.shields.io/badge/python-3.x-blue)
# Myrmecology XML CLI Tool

A simple CLI tool for validating and converting XML files using Python.

## Description

This project is a command-line tool for working with XML data. It allows validating XML files against an XSD schema and converting XML data into JSON format.

The dataset describes ants, their biology, colony structure, and selected species.

## Features

- XML validation using XSD schema
- XML → JSON conversion
- Command Line Interface (CLI) built with Typer
- Verbose mode ('-v', '--verbose')
- Colored output and user-friendly error handling
- Modular Python structure

## Technologies

- Python 3
- typer – CLI interface
- lxml – XML validation
- xmltodict – XML parsing

## Project Structure

``` txt
.
├── xml_utils/
│   ├── cli.py         # CLI interface (Typer)
│   ├── parse.py       # XML → JSON conversion
│   ├── validate.py    # XML validation logic
│
├── examples/
│   ├── valid.xml
│   ├── invalid.xml
│   └── output.json
│
├── schema.xsd
├── main.py            # Entry point
├── requirements.txt
└── README.md
```

## Installation
```bash
pip install -r requirements.txt
```
## Usage

### Show help:
```bash
python main.py --help
```
### Validate XML
```bash
python main.py validate examples/valid.xml schema.xsd
```

- With verbose output:
```bash
python main.py validate examples/valid.xml schema.xsd -v
```
### Convert XML to JSON
```bash
python main.py parse examples/valid.xml examples/output.json
```
- With verbose output:
```bash
python main.py parse examples/valid.xml examples/output.json -v
```
## Example Data

The XML structure includes:
- Author information
- Ant anatomy
- Colony hierarchy (queen, workers, males)
- Species descriptions

## Error Handling

The CLI provides:
- Clear error messages
- Colored output
- Proper exit codes (0 for success, 1 for errors)

## Purpose

This project was created to practice:

- XML structure design
- XSD schema validation
- Data transformation (XML → JSON)
- Building CLI tools in Python

## Possible Improvements

- Add unit tests (pytest)
- Add logging system
- Create REST API (e.g., FastAPI)
- Package as installable CLI tool

## Author

jack-and-his-ants