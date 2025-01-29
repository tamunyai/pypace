from pypace.models import Arc, Saga


def test_saga_add_arc():
    saga = Saga(name="East Blue")
    arc = Arc(name="Syrup Village", chapters=(22, 41))

    saga.add_arc(arc)

    assert len(saga.arcs) == 1
    assert saga.arcs[0].name == "Syrup Village"
