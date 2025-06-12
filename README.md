# File/Directory Search Tool

A Python script to search for files or directories based on name matching (exact or partial) within a specified directory tree.

## Features

- Search for files or directories by name
- Choose between exact name matches or partial containment
- Recursively search through all subdirectories
- Simple command-line interface

## Installation

1. Ensure you have Python 3.x installed on your system
2. Clone this repository or download the script directly


git clone https://github.com/your-username/your-repo-name.git

## Usage

Run the script from the command line:
bash

python search_tool.py

The script will prompt you for:

    The directory path to search in

    Whether you're looking for a file or directory

    The name to search for

    Whether to match the name exactly or just contain the text

## Examples

    Find all Python files exactly named "config":
    text

Where do you want to search?: /projects
Are you looking for a file or a directory? (file/directory): file
What name are you looking for?: config
Should the name match exactly or just contain it? (exact/contain): exact

Find all directories containing "temp" in their name:
text

    Where do you want to search?: C:\Users
    Are you looking for a file or a directory? (file/directory): directory
    What name are you looking for?: temp
    Should the name match exactly or just contain it? (exact/contain): contain

Requirements

    Python 3.x

    Standard Python libraries (only os module required)

Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.
License

MIT License
Future Improvements

    Add support for regular expressions

    Implement case-insensitive search option

    Add file size and modification date filters

    Create a GUI version
