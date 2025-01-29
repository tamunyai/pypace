# Pypace - OnePace File Organizer

**Pypace** is a Python command-line tool designed to organize [OnePace](https://onepace.net) files within a user-specified directory. **OnePace** is a fan project that recuts the **One Piece** anime to align more closely with the pacing of the original manga by Eiichiro Oda. This tool sorts the files based on their respective saga and arc, according to the structure defined in the [One Piece Wiki](https://onepiece.fandom.com/wiki/Story_Arcs).

## Features

- Automatically organizes **OnePace** files into directories based on saga and arc names.
- Creates a directory structure that mirrors the sagas and arcs of the **One Piece** anime series.
- Logs progress with color-coded messages indicating the status of file movements (e.g., success, warnings).
- Skips files that already exist in the destination directory to prevent overwriting.
- Command-line interface for easier usage.
- Supports "dry-run" mode to preview file movements without making changes.
- Resets files to their original location if needed.

## Requirements

- Python 3.6 or higher.
- The script assumes that OnePace files are named with the string "[One Pace]" to identify them.
- The required Python libraries:
  - `colorama` (for colored output)
  - `pytest` and `pytest-mock` (for testing)
  - `shutil`, `logging`, `pathlib`, and `re` modules (all standard in Python) are used.

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

Alternatively, you can install `pypace` via pip if you have already set up the package:

```bash
pip install pypace
```

## Installation

1. Download or clone this repository to your local machine.
2. Navigate to the directory containing the project.
3. Install dependencies via pip (make sure Python 3.6+ is installed):

```bash
pip install .
```

## Usage

### Command-Line Interface (CLI)

To run the tool from the command line, use the following command:

```bash
pypace /path/to/your/directory
```

You can also specify the --dry-run option to preview the file movements without making actual changes:

```bash
pypace /path/to/your/directory --dry-run
```

If you need to reset the file organization to their original locations, use the --reset option:

```bash
pypace /path/to/your/directory --reset
```

### Directory Structure

The script organizes the files into a structure like this:

```bash
<base_directory>
├── 01 - East Blue Saga
│   ├── 011 - Romance Dawn Arc
│   ├── 012 - Orange Town Arc
│   └── ...
├── 02 - Arabasta Saga
│   ├── 021 - Reverse Mountain Arc
│   ├── 022 - Whisky Peak Arc
│   └── ...
└── ...
```

Each saga and arc is given a numbered prefix to ensure proper sorting.

### Customization

- **Base Directory**: The directory where the OnePace files are located can be specified when running the CLI tool. This is provided as an argument when running the `pypace` command.
- **Sagas and Arcs**: The predefined sagas and arcs (from the One Piece anime) are included in the tool, but you can modify the list of sagas and arcs in the script if you'd like to tailor the tool for a custom collection.

### Example Usage in Python

You can also use `pypace` directly in Python code like this:

```python
from pypace import organize_files

organize_files("/path/to/your/directory", dry_run=True)
```

### Resetting Files

If you want to reset the file organization back to their original location, you can use the --reset flag:

```bash
pypace /path/to/your/directory --reset
```

This will restore the files to their original location within the base directory.

## Testing

This project comes with a set of unit tests to ensure proper functionality, using `pytest` and `pytest-mock` for mocking dependencies and verifying the tool’s behavior.

### Running Tests

To run the tests:

```bash
pytest
```

Make sure the necessary dependencies are installed first:

```bash
pip install pytest pytest-mock
```

Tests are located in the `tests` directory, which includes tests for individual components, such as file organization, CLI functionality, and the episode handling logic.

## License

This project is open-source and free to use, modify, and distribute under the [MIT License](license).

## Disclaimer

This script is a utility tool for organizing files related to the **OnePace** fan project, which is an unofficial recut of the **One Piece** anime. This is not affiliated with the official creators of **One Piece** or **OnePace**.
