# File Organizer Script

This Python script organizes files in a specified directory based on their file extensions. It helps categorize various file types into designated folders within a given directory.

## Overview

The script utilizes predefined lists of file extensions (`EXT_AUDIO`, `EXT_VIDEO`, `EXT_IMAGE`, `EXT_DOC`, `EXT_COMP`, `EXT_APP`) to sort files into corresponding folders (`Downloads`, `Music`, `Images`, `Videos`, `Docs`, `Apps`, `others`). It scans the `Downloads` directory (you can modify the base path) and moves files to their appropriate destinations.

## Getting Started

1. **Clone Repository:** Clone this repository to your local machine.
2. **Python Environment:** Ensure you have Python installed (version 3.6 or higher).
3. **Modify Path:** Replace `'YOUR PATH HERE/'` in the script with your desired base path.
4. **Execute Script:** Run the script using Python.

## Usage

The script operates as follows:

- Creates directories for specific file types if they don't exist.
- Scans files within the `Downloads` directory.
- Organizes files into respective folders based on their extensions.

```python
# Replace 'YOUR PATH HERE/' with the desired base path
pathB = 'YOUR PATH HERE/'

# Run the script
# Example usage:
# python file_organizer.py
