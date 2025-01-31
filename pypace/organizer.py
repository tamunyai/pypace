import logging
import shutil
from pathlib import Path

from colorama import Fore, Style, init

from .data import SAGAS_WITH_ARCS
from .models import Episode

init(autoreset=True)

logging.basicConfig(
    format=f"{Fore.CYAN}%(levelname)s:{Style.RESET_ALL} %(message)s",
    level=logging.INFO,
)


def is_one_pace_file(file: Path) -> bool:
    """
    Check if a given file is a One Pace episode.

    Args:
        file (Path): The file to check.

    Returns:
        bool: True if the file is a One Pace episode, False otherwise.
    """
    return file.is_file() and "[One Pace]" in file.stem


def organize_files(directory: Path, dry_run: bool):
    """
    Organizes One Pace episodes into their respective saga and arc folders.

    Args:
        directory (Path): The root directory containing the episodes.
        dry_run (bool): If True, only logs actions without making changes.
    """
    if not directory.is_dir():
        logging.error(f"{Fore.RED}Invalid directory:{Style.RESET_ALL} {directory}")
        return

    # if not directory.exists():
    #     logging.error(f"{Fore.RED}Invalid directory:{Style.RESET_ALL} {directory}")
    #     return

    arc_lookup = {
        arc_name: arc
        for saga in SAGAS_WITH_ARCS
        for arc in saga.arcs
        for arc_name in arc.all_names
    }

    for file in directory.rglob("*"):
        if not is_one_pace_file(file):
            continue

        try:
            episode = Episode(filepath=file)

        except ValueError as e:
            logging.warning(f"{Fore.YELLOW}Skipping:{Style.RESET_ALL} {file} → {e}")
            continue

        arc = arc_lookup.get(episode.arc_name)
        if arc:
            arc.add_episode(episode)
        else:
            logging.warning(f"{Fore.YELLOW}No matching arc:{Style.RESET_ALL} {file}")
            continue

    files_moved_count = 0
    for saga_index, saga in enumerate(SAGAS_WITH_ARCS, 1):
        saga_folder = directory / f"{saga_index:02} - {saga.actual_name}"

        for arc_index, arc in enumerate(saga.arcs, 1):
            arc_folder = saga_folder / f"{saga_index:02}{arc_index} - {arc.actual_name}"

            for episode in arc.episodes:
                target_path = arc_folder / episode.filepath.name

                if target_path.exists():
                    continue

                if not dry_run:
                    arc_folder.mkdir(parents=True, exist_ok=True)
                    shutil.move(episode.filepath, target_path)

                logging.info(
                    f"{Fore.GREEN}Moved:{Style.RESET_ALL} {episode.filepath} → {target_path}"
                )
                files_moved_count += 1

    logging.info(
        f"{Fore.MAGENTA}Total files moved:{Style.RESET_ALL} {files_moved_count}"
    )


def reset(directory: Path, dry_run: bool):
    """
    Moves all One Pace episodes back to the root directory.

    Args:
        directory (Path): The root directory containing the episodes.
        dry_run (bool): If True, only logs actions without making changes.
    """
    for file in directory.rglob("*"):
        if not is_one_pace_file(file):
            continue

        target_path = directory / file.name
        if not dry_run:
            shutil.move(file, target_path)

        logging.info(f"{Fore.BLUE}Reset:{Style.RESET_ALL} {file} → {target_path}")
