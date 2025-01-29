import pytest

from pypace.models import Episode

from .utils import mock_file


def test_episode_init_valid():
    file = mock_file("[One Pace][941-942] Wano 22 [720p][En Sub][CA70257D]")
    episode = Episode(filepath=file)

    assert episode.arc_name == "Wano"
    assert episode.episode_number == 22
    assert episode.chapters == [(941, 942)]
    assert episode.covered_chapters == set(range(941, 943))


def test_episode_init_invalid_filename():
    file = mock_file("Invalid_Episode_Name")
    with pytest.raises(ValueError, match="Filename does not match expected format"):
        Episode(filepath=file)
