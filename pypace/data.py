from .models import Arc, Saga

SAGAS_WITH_ARCS = [
    Saga(
        name="East Blue",
        arcs=[
            Arc(name="Romance Dawn", chapters=(1, 7)),
            Arc(name="Orange Town", chapters=(8, 21)),
            Arc(name="Syrup Village", chapters=(22, 41)),
            Arc(name="Baratie", chapters=(42, 68)),
            Arc(name="Arlong Park", chapters=(69, 95)),
            Arc(name="Loguetown", chapters=(96, 100)),
        ],
    ),
    Saga(
        name="Arabasta",
        arcs=[
            Arc(name="Reverse Mountain", chapters=(101, 105)),
            Arc(name="Whisky Peak", chapters=(106, 114)),
            Arc(name="Little Garden", chapters=(115, 129)),
            Arc(name="Drum Island", chapters=(130, 154)),
            Arc(name="Arabasta", chapters=(155, 217)),
        ],
    ),
    Saga(
        name="Sky Island",
        arcs=[
            Arc(name="Jaya", chapters=(218, 236)),
            Arc(name="Skypiea", chapters=(237, 302)),
        ],
    ),
    Saga(
        name="Water 7",
        aliases=["Water Seven"],
        arcs=[
            Arc(name="Long Ring Long Land", chapters=(303, 321)),
            Arc(name="Water 7", aliases=["Water Seven"], chapters=(322, 374)),
            Arc(name="Enies Lobby", chapters=(375, 430)),
            Arc(name="Post-Enies Lobby", chapters=(431, 441)),
        ],
    ),
    Saga(
        name="Thriller Bark",
        arcs=[
            Arc(name="Thriller Bark", chapters=(442, 489)),
        ],
    ),
    Saga(
        name="Summit War",
        arcs=[
            Arc(name="Sabaody Archipelago", chapters=(490, 513)),
            Arc(name="Amazon Lily", chapters=(514, 524)),
            Arc(name="Impel Down", chapters=(525, 549)),
            Arc(name="Marineford", chapters=(550, 580)),
            Arc(name="Post-War", chapters=(581, 597)),
        ],
    ),
    Saga(
        name="Fish-Man Island",
        aliases=["Fishman Island"],
        arcs=[
            Arc(name="Return to Sabaody", chapters=(598, 602)),
            Arc(
                name="Fish-Man Island", aliases=["Fishman Island"], chapters=(603, 653)
            ),
        ],
    ),
    Saga(
        name="Dressrosa",
        arcs=[
            Arc(name="Punk Hazard", chapters=(654, 699)),
            Arc(name="Dressrosa", chapters=(700, 801)),
        ],
    ),
    Saga(
        name="Whole Cake Island",
        arcs=[
            Arc(name="Zou", chapters=(802, 824)),
            Arc(name="Whole Cake Island", chapters=(825, 902)),
            Arc(name="Levely", aliases=["Reverie"], chapters=(903, 908)),
        ],
    ),
    Saga(
        name="Wano Country",
        arcs=[
            Arc(name="Wano Country", aliases=["Wano"], chapters=(909, 1057)),
        ],
    ),
    Saga(
        name="Final",
        arcs=[
            Arc(name="EggHead", chapters=(1058, 1125)),
            Arc(name="Elbaph"),  # 1126-present
        ],
    ),
]
