#!/usr/bin/env python3

import logging
from pathlib import Path
from re import IGNORECASE, escape, search, sub
from shutil import move

# ANSI escape codes for colors
RESET_COLOR = "\033[0m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
CYAN = "\033[0;36m"


class OnePaceFileOrganizer:
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
    )

    def __init__(self, base_directory: str = "./") -> None:
        """
        Initializes the file organizer with the specified base directory and predefined saga and arc structure.

        Args:
            base_directory (str, optional): The directory where OnePace files are stored (default: current directory).
        """
        self.base_directory = Path(base_directory)
        self.one_pace_files = self._get_one_pace_files()
        self.sagas_with_arcs = self._get_sagas_with_arcs()
        self.files_by_arc = self._organize_files_by_arc()

    def _get_one_pace_files(self) -> list[Path]:
        """
        Retrieves all files in the base directory that are related to OnePace, identified by '[One Pace]' in the filename.

        Returns:
            list[Path] :A list of Path objects representing the OnePace files found in the base directory.
        """
        return [
            file
            for file in self.base_directory.iterdir()
            if file.is_file() and "[One Pace]" in file.name
        ]

    def _get_sagas_with_arcs(self) -> dict[str, list[str]]:
        """
        Returns a dictionary mapping each saga to its corresponding arcs in the OnePiece series.

        Returns:
            dict[str, list[str]]: A dictionary where the keys are saga names (e.g., "East Blue Saga") and the values are lists of arc names.
        """
        return {
            "East Blue Saga": [
                "Romance Dawn Arc",
                "Orange Town Arc",
                "Syrup Village Arc",
                "Baratie Arc",
                "Arlong Park Arc",
                "Loguetown Arc",
            ],
            "Arabasta Saga": [
                "Reverse Mountain Arc",
                "Whisky Peak Arc",
                "Little Garden Arc",
                "Drum Island Arc",
                "Arabasta Arc",
            ],
            "Sky Island Saga": ["Jaya Arc", "Skypiea Arc"],
            "Water Seven Saga": [
                "Long Ring Long Land Arc",
                "Water Seven Arc",
                "Enies Lobby Arc",
                "Post-Enies Lobby Arc",
            ],
            "Thriller Bark Saga": ["Thriller Bark Arc"],
            "Summit War Saga": [
                "Sabaody Archipelago Arc",
                "Amazon Lily Arc",
                "Impel Down Arc",
                "Marineford Arc",
                "Post-War Arc",
            ],
            "Fish-Man Island Saga": ["Return to Sabaody Arc", "Fish-Man Arc"],
            "Dressrosa Saga": ["Punk Hazard Arc", "Dressrosa Arc"],
            "Whole Cake Island Saga": ["Zou Arc", "Whole Cake Arc", "Levely Arc"],
            "Wano Country Saga": ["Wano Country Arc"],
            "Final Saga": ["EggHead Arc", "Elbaph Arc"],
        }

    def _organize_files_by_arc(self) -> dict[str, list[Path]]:
        """
        Organizes OnePace files by arc names, associating each arc with the relevant files in the base directory.

        Returns:
            dict[str, list[Path]]: A dictionary where keys are arc names (without "Arc" suffix) and values are lists of files for each arc.
        """
        files_by_arc = {}
        for file in self.one_pace_files:
            for arcs in self.sagas_with_arcs.values():
                for arc_name in arcs:
                    arc_name_without_suffix = sub(r" Arc$", "", arc_name)
                    # arc_name_without_suffix = escape(arc_name_without_suffix)
                    pattern = rf"\s{arc_name_without_suffix}\s"

                    if not search(pattern, file.name, IGNORECASE):
                        continue

                    if arc_name_without_suffix not in files_by_arc:
                        files_by_arc[arc_name_without_suffix] = []

                    files_by_arc[arc_name_without_suffix].append(file)

        return files_by_arc

    def _create_directory_if_not_exists(self, directory: Path):
        """
        Creates a directory if it doesn't already exist.

        Args:
            directory (Path): The path to the directory to be created if it doesn't exist.
        """
        if not directory.exists():
            logging.info(f"{CYAN}Creating directory: {directory}{RESET_COLOR}")
            directory.mkdir(parents=True, exist_ok=True)

    def _move_file(self, source_path: Path, destination_path: Path) -> bool:
        """
        Attempts to move a file from source to destination.

        Args:
            source_path (Path): The source file path.
            destination_path (Path): The destination path where the file will be moved.

        Returns:
            bool: True if the file was moved successfully, False otherwise.
        """
        try:
            if destination_path.exists():
                logging.warning(
                    f"{RED}Destination file {destination_path} already exists, skipping.{RESET_COLOR}"
                )
                return False

            logging.info(f"{YELLOW}Moving: {source_path.name}{RESET_COLOR}")
            move(source_path, destination_path)
            logging.info(f"{GREEN}Moved: {destination_path}{RESET_COLOR}")
            return True

        except Exception as e:
            logging.error(f"{RED}Error moving {source_path.name}: {e}{RESET_COLOR}")
            return False

    def _organize_arc(
        self, saga_index: int, saga_name: str, arc_index: int, arc_name: str
    ) -> int:
        """
        Organizes the files associated with a specific arc by moving them into the correct directory.

        Args:
            saga_index (int): The index of the saga in the overall series.
            saga_name (int): The name of the saga (e.g., "East Blue Saga").
            arc_index (int): The index of the arc within the saga.
            arc_name (int): The name of the arc (e.g., "Romance Dawn Arc").

        Returns:
            int: The number of files successfully moved for this arc.
        """
        arc_name_without_suffix = sub(r" Arc$", "", arc_name)
        saga_directory = self.base_directory / f"{saga_index:02} - {saga_name}"
        arc_directory = saga_directory / f"{saga_index:02}{arc_index} - {arc_name}"

        count = 0
        files_for_arc = self.files_by_arc.get(arc_name_without_suffix, [])
        for file in files_for_arc:
            source_path = self.base_directory / file.name
            destination_path = arc_directory / file.name

            self._create_directory_if_not_exists(arc_directory)
            if self._move_file(source_path, destination_path):
                count += 1

        return count

    def organize_files(self):
        """
        Organizes OnePace files by their saga and arc by moving them into appropriate directories.
        """
        files_moved_count = 0
        for saga_index, (saga_name, arcs) in enumerate(self.sagas_with_arcs.items(), 1):
            for arc_index, arc_name in enumerate(arcs, 1):
                files_moved_count += self._organize_arc(
                    saga_index, saga_name, arc_index, arc_name
                )

        logging.info(f"Total files moved: {files_moved_count}")

    def run(self):
        """
        Executes the file organization process.
        """
        logging.info(f"Starting file organization in '{self.base_directory.resolve()}'")
        self.organize_files()
        logging.info(f"File organization completed.")


if __name__ == "__main__":
    organizer = OnePaceFileOrganizer()
    organizer.run()
