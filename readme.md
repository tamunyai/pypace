# OnePace File Organizer

The **OnePace File Organizer** is a Python script designed to organize [OnePace](https://onepace.net) files within a user-specified directory. **OnePace** is a fan project that recuts the **One Piece** anime to align more closely with the pacing of the original manga by Eiichiro Oda. This tool sorts the files based on their respective saga and arc, according to the structure defined in the [One Piece Wiki](https://onepiece.fandom.com/wiki/Story_Arcs).

## Features

- Automatically organizes OnePace files into directories based on saga and arc names.
- Creates a directory structure that mirrors the sagas and arcs of the **One Piece** anime series.
- Logs progress with color-coded messages indicating the status of file movements (e.g., success, warnings).
- Skips files that already exist in the destination directory to prevent overwriting.

## Requirements

- Python 3.6 or higher.
- The script assumes that OnePace files are named with the string "[One Pace]" to identify them.
- The required `shutil`, `logging`, `pathlib`, and `re` modules (all standard in Python) are used.

## Installation

1. Download or clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Ensure that your OnePace files are located in the base directory (by default, the current directory).

## Usage

### Running the Script

To run the script, use the following command:

```bash
python3 onepace_file_organizer.py
```

By default, the script will organize files in the current directory. If you want to specify a different directory, pass the path to the directory as an argument when initializing the `OnePaceFileOrganizer` class:

```python
organizer = OnePaceFileOrganizer(base_directory="path/to/your/directory")
```

### Directory Structure

The script organizes the files into a structure like this:

```bash
<base_directory>
├── 01 - East Blue Saga
│   ├── 01 - Romance Dawn Arc
│   ├── 02 - Orange Town Arc
│   └── ...
├── 02 - Arabasta Saga
│   ├── 01 - Reverse Mountain Arc
│   ├── 02 - Whisky Peak Arc
│   └── ...
└── ...
```

Each saga and arc is given a numbered prefix to ensure proper sorting.

## Customization

### Base Directory

The base directory is configurable by changing the `base_directory` argument when initializing the `OnePaceFileOrganizer` object.

### Saga and Arc Structure

The saga and arc structure is predefined in the script, but you can modify the `_get_sagas_with_arcs` method to suit custom projects or different naming conventions.

## Disclaimer

This script is a utility tool for organizing files related to the **OnePace** fan project, which is an unofficial recut of the **One Piece** anime. This is not affiliated with the official creators of **One Piece** or **OnePace**.
