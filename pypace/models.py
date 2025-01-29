import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple, Union


@dataclass
class Episode:
    filepath: Path

    arc_name: str = field(init=False, repr=False)
    episode_number: int = field(init=False, repr=False)
    chapters: List[Union[Tuple[int, int], int]] = field(init=False)
    covered_chapters: set = field(init=False, default_factory=set)

    def __post_init__(self):
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
    name: str
    chapters: Optional[Tuple[int, int]] = None
    aliases: List[str] = field(default_factory=list)
    episodes: List[Episode] = field(repr=False, default_factory=list)
    covered_chapters: set = field(init=False, default_factory=set)

    def add_episode(self, episode: Episode) -> None:
        self.episodes.append(episode)
        self.covered_chapters.update(episode.covered_chapters)

    @property
    def actual_name(self) -> str:
        return f"{self.name} Arc"

    @property
    def all_names(self) -> List[str]:
        return [self.name] + self.aliases

    @property
    def completed(self) -> bool:
        if not self.chapters:
            raise ValueError(f"{self.name} Arc chapters range is not defined.")

        arc_start, arc_end = self.chapters
        required_chapters = set(range(arc_start, arc_end + 1))
        return required_chapters.issubset(self.covered_chapters)

    def missing_chapters(self) -> List[int]:
        if not self.chapters:
            raise ValueError(f"{self.name} Arc chapters range is not defined.")

        arc_start, arc_end = self.chapters
        required_chapters = set(range(arc_start, arc_end + 1))
        return list(required_chapters - self.covered_chapters)


@dataclass
class Saga:
    name: str
    aliases: List[str] = field(default_factory=list)
    arcs: List[Arc] = field(default_factory=list)

    def add_arc(self, arc: Arc):
        self.arcs.append(arc)

    @property
    def actual_name(self) -> str:
        return f"{self.name} Saga"

    @property
    def all_names(self) -> List[str]:
        return [self.name] + self.aliases

    @property
    def completed(self) -> bool:
        return all([arc.completed for arc in self.arcs])

    def missing_arcs(self) -> List[str]:
        return [arc.actual_name for arc in self.arcs if not arc.completed]
