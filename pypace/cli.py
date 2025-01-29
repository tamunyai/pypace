import argparse
from pathlib import Path

from colorama import Fore, Style

from .organizer import organize_files, reset


def main():
    parser = argparse.ArgumentParser(
        description="Organize One Pace files into sagas and arcs."
    )
    parser.add_argument("directory", help="Directory containing One Pace files.")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes.")
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Move files back.",
    )

    args = parser.parse_args()
    directory = Path(args.directory).resolve()

    print(f"{Fore.CYAN}Processing Directory: {Style.RESET_ALL}{directory}")

    if args.reset:
        print(f"{Fore.YELLOW}Resetting files...{Style.RESET_ALL}")
        reset(directory, args.dry_run)
    else:
        print(f"{Fore.GREEN}Organizing files...{Style.RESET_ALL}")
        organize_files(directory, args.dry_run)


if __name__ == "__main__":
    main()
