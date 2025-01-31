import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple, Union


@dataclass
class Episode:
    """
    Represents an individual One Pace episode.

    Attributes:
        filepath (Path): The file path of the episode.
        arc_name (str): The name of the arc this episode belongs to.
        episode_number (int): The episode number within the arc.
        chapters (List[Union[Tuple[int, int], int]]): A list of chapters covered in this episode.
        covered_chapters (set): A set of chapter numbers covered in this episode.
    """
    filepath: Path

    arc_name: str = field(init=False, repr=False)
    episode_number: int = field(init=False, repr=False)
    chapters: List[Union[Tuple[int, int], int]] = field(init=False)
    covered_chapters: set = field(init=False, default_factory=set)

    def __post_init__(self):
        """
        Parses the filename to extract arc name, episode number, and covered chapters.

        Raises:
            ValueError: If the file does not exist, the filename format is incorrect,
                        or no valid chapters are found.
        """
        if not self.filepath.exists():
            raise ValueError(f"File does not exist: {self.filepath}")

        # Extract arc name and episode number from the filename
        match = re.search(r"\] (.*?) \[", self.filepath.stem)
        if not match:
            raise ValueError(
                f"Filename does not match expected format: {self.filepath.stem}"
            )

        parts: list = match.group(1).strip().split(" ")
        self.arc_name = " ".join(parts[:-1]).strip()
        self.episode_number = int(parts[-1])

        # Extract chapters information from the filename
        matches = re.findall(r"\[([^\]]+)\]", self.filepath.stem)
        chapters_info = re.findall(r"(\d+)(?:-(\d+))?", matches[1])

        self.chapters = []
        for start, end in chapters_info:
            if end:
                self.chapters.append((int(start), int(end)))
                self.covered_chapters.update(range(int(start), int(end) + 1))

            else:
                self.chapters.append(int(start))
                self.covered_chapters.add(int(start))

        if not self.chapters:
            raise ValueError("No valid chapters found in the input string.")


@dataclass
class Arc:
    """
    Represents an arc within a One Pace saga.

    Attributes:
        name (str): The name of the arc.
        chapters (Optional[Tuple[int, int]]): The range of chapters covered in this arc.
        aliases (List[str]): Alternative names for the arc.
        episodes (List[Episode]): The episodes belonging to this arc.
        covered_chapters (set): The set of chapters covered by all episodes in the arc.
    """
    name: str
    chapters: Optional[Tuple[int, int]] = None
    aliases: List[str] = field(default_factory=list)
    episodes: List[Episode] = field(repr=False, default_factory=list)
    covered_chapters: set = field(init=False, default_factory=set)

    def add_episode(self, episode: Episode) -> None:
        """
        Adds an episode to the arc and updates the covered chapters.

        Args:
            episode (Episode): The episode to be added.
        """
        self.episodes.append(episode)
        self.covered_chapters.update(episode.covered_chapters)

    @property
    def actual_name(self) -> str:
        """
        Returns the full name of the arc.

        Returns:
            str: The formatted arc name.
        """
        return f"{self.name} Arc"

    @property
    def all_names(self) -> List[str]:
        """
        Returns all known names (including aliases) for this arc.

        Returns:
            List[str]: A list of names associated with this arc.
        """
        return [self.name] + self.aliases

    @property
    def completed(self) -> bool:
        """
        Determines if all chapters in the arc have been covered by episodes.

        Returns:
            bool: True if all chapters are covered, False otherwise.

        Raises:
            ValueError: If the chapter range is not defined.
        """
        if not self.chapters:
            raise ValueError(f"{self.name} Arc chapters range is not defined.")

        arc_start, arc_end = self.chapters
        required_chapters = set(range(arc_start, arc_end + 1))
        return required_chapters.issubset(self.covered_chapters)

    def missing_chapters(self) -> List[int]:
        """
        Returns a list of chapters that are not yet covered.

        Returns:
            List[int]: A list of missing chapter numbers.

        Raises:
            ValueError: If the chapter range is not defined.
        """
        if not self.chapters:
            raise ValueError(f"{self.name} Arc chapters range is not defined.")

        arc_start, arc_end = self.chapters
        required_chapters = set(range(arc_start, arc_end + 1))
        return list(required_chapters - self.covered_chapters)


@dataclass
class Saga:
    """
    Represents a saga containing multiple arcs.

    Attributes:
        name (str): The name of the saga.
        aliases (List[str]): Alternative names for the saga.
        arcs (List[Arc]): The arcs that belong to this saga.
    """
    name: str
    aliases: List[str] = field(default_factory=list)
    arcs: List[Arc] = field(default_factory=list)

    def add_arc(self, arc: Arc):
        """
        Adds an arc to the saga.

        Args:
            arc (Arc): The arc to be added.
        """
        self.arcs.append(arc)

    @property
    def actual_name(self) -> str:
        """
        Returns the full name of the saga.

        Returns:
            str: The formatted saga name.
        """
        return f"{self.name} Saga"

    @property
    def all_names(self) -> List[str]:
        """
        Returns all known names (including aliases) for this saga.

        Returns:
            List[str]: A list of names associated with this saga.
        """
        return [self.name] + self.aliases

    @property
    def completed(self) -> bool:
        """
        Determines if all arcs within the saga are completed.

        Returns:
            bool: True if all arcs are completed, False otherwise.
        """
        return all([arc.completed for arc in self.arcs])

    def missing_arcs(self) -> List[str]:
        """
        Returns a list of arcs that are not yet completed.

        Returns:
            List[str]: A list of arc names that are missing episodes.
        """
        return [arc.actual_name for arc in self.arcs if not arc.completed]
