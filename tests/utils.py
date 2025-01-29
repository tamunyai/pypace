from pathlib import Path
from unittest import mock


# Helper function to mock a file with a given name
def mock_file(filename: str):
    file_mock = mock.MagicMock(spec=Path)
    file_mock.stem = filename
    file_mock.is_file.return_value = True
    file_mock.exists.return_value = True
    return file_mock
