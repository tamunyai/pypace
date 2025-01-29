import argparse

from .organizer import OnePaceFileOrganizer


def main():
    parser = argparse.ArgumentParser(
        description="Organize One Pace files into sagas and arcs."
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory containing One Pace files (default: current directory)",
    )
    args = parser.parse_args()
    organizer = OnePaceFileOrganizer(args.directory)
    organizer.organize_files()


if __name__ == "__main__":
    main()
