import pytest

from test_3.main import Map, PathFinder, Point, Raft, Water, Land

@pytest.fixture
def water_map() -> tuple:
    field = Map().random(m=10, n=10, land_percent=0)
    shortest_way = [
        Point(x=0, y=0),
        Point(x=1, y=0),
        Point(x=2, y=0),
        Point(x=3, y=0),
        Point(x=4, y=0),
        Point(x=5, y=0),
        Point(x=6, y=0),
        Point(x=7, y=0),
        Point(x=8, y=0),
        Point(x=9, y=0),
        Point(x=9, y=1),
        Point(x=9, y=2),
        Point(x=9, y=3),
        Point(x=9, y=4),
        Point(x=9, y=5),
        Point(x=9, y=6),
        Point(x=9, y=7),
        Point(x=9, y=8),
        Point(x=9, y=9),
    ]
    return field, shortest_way


@pytest.fixture
def medium_map() -> tuple:
    list_of_cells = [
            Water(x=0, y=0),
            Water(x=0, y=1),
            Water(x=0, y=2),
            Land(x=0, y=3),
            Water(x=0, y=4),
            Land(x=1, y=0),
            Land(x=1, y=1),
            Water(x=1, y=2),
            Water(x=1, y=3),
            Water(x=1, y=4),
            Water(x=2, y=0),
            Water(x=2, y=1),
            Water(x=2, y=2),
            Water(x=2, y=3),
            Water(x=2, y=4),
            Water(x=3, y=0),
            Water(x=3, y=1),
            Land(x=3, y=2),
            Land(x=3, y=3),
            Land(x=3, y=4),
            Water(x=4, y=0),
            Water(x=4, y=1),
            Water(x=4, y=2),
            Water(x=4, y=3),
            Water(x=4, y=4),
        ]
    field = dict()
    for cell in list_of_cells:
        field[str(hash(cell))] = cell

    field = Map(_m=5, _n=5, field=field)
    shortest_way = [
        Point(x=0, y=0),
        Point(x=0, y=1),
        Point(x=0, y=2),
        Point(x=1, y=2),
        Point(x=2, y=2),
        Point(x=2, y=1),
        Point(x=3, y=1),
        Point(x=4, y=1),
        Point(x=4, y=2),
        Point(x=4, y=3),
        Point(x=4, y=4),
    ]
    return field, shortest_way


@pytest.fixture
def map_without_way() -> tuple:
    list_of_cells = [
            Water(x=0, y=0),
            Water(x=0, y=1),
            Water(x=0, y=2),
            Land(x=0, y=3),
            Water(x=0, y=4),
            Land(x=1, y=0),
            Land(x=1, y=1),
            Water(x=1, y=2),
            Water(x=1, y=3),
            Water(x=1, y=4),
            Water(x=2, y=0),
            Water(x=2, y=1),
            Water(x=2, y=2),
            Water(x=2, y=3),
            Water(x=2, y=4),
            Land(x=3, y=0),
            Land(x=3, y=1),
            Land(x=3, y=2),
            Land(x=3, y=3),
            Land(x=3, y=4),
            Land(x=4, y=0),
            Land(x=4, y=1),
            Land(x=4, y=2),
            Land(x=4, y=3),
            Water(x=4, y=4),
        ]
    field = dict()
    for cell in list_of_cells:
        field[str(hash(cell))] = cell

    field = Map(_m=5, _n=5, field=field)
    shortest_way = [
    ]
    return field, shortest_way