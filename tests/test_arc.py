from pypace.models import Arc, Episode

from .utils import mock_file


def test_arc_add_episode():
    arc = Arc(name="Orange Town", chapters=(8, 21))
    file = mock_file("[One Pace][8-11] Orange Town 01 [720p][En Sub][D57B5C12]")
    episode = Episode(filepath=file)

    arc.add_episode(episode)

    assert len(arc.episodes) == 1
    assert arc.covered_chapters == set(range(8, 12))


def test_arc_completed():
    arc = Arc(name="Orange Town", chapters=(8, 21))
    file1 = mock_file("[One Pace][8-11] Orange Town 01 [720p][En Sub][D57B5C12]")
    file2 = mock_file("[One Pace][12-19] Orange Town 02 [720p][En Sub][0BE187AB]")
    file3 = mock_file("[One Pace][19-21] Orange Town 03 [720p][En Sub][FC1B9A25]")
    episode1 = Episode(filepath=file1)
    episode2 = Episode(filepath=file2)
    episode3 = Episode(filepath=file3)

    arc.add_episode(episode1)
    arc.add_episode(episode2)
    arc.add_episode(episode3)

    assert arc.completed is True
