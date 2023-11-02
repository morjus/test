from test_3.main import PathFinder, Point, Raft


def test_shortest_way_easy(water_map):
    field, shortest_way = water_map
    start = Point(x=0, y=0)
    end = Point(x=9, y=9)
    raft = Raft(x=0, y=0)
    path_finder = PathFinder(map=field, start=start, end=end, raft=raft)
    path = path_finder.find_shortest_way()
    assert path == shortest_way, "Incorrect shortest way!"


def test_shortest_way_hard(medium_map):
    field, shortest_way = medium_map
    start = Point(x=0, y=0)
    end = Point(x=4, y=4)
    raft = Raft(x=0, y=0)
    path_finder = PathFinder(map=field, start=start, end=end, raft=raft)
    path = path_finder.find_shortest_way()
    assert path == shortest_way, "Incorrect shortest way!"


def test_start_point_out_of_the_map(water_map):
    field, _ = water_map
    start = Point(x=100, y=100)
    end = Point(x=0, y=0)
    raft = Raft(x=0, y=0)
    path_finder = PathFinder(map=field, start=start, end=end, raft=raft)
    path = path_finder.find_shortest_way()
    assert path == [], "Incorrect shortest way!"


def test_no_way_to_the_end(map_without_way):
    field, shortest_way = map_without_way
    start = Point(x=0, y=0)
    end = Point(x=4, y=4)
    raft = Raft(x=0, y=0)
    path_finder = PathFinder(map=field, start=start, end=end, raft=raft)
    path = path_finder.find_shortest_way()
    assert path == shortest_way, "Incorrect shortest way!"


def test_end_point_out_of_the_map(water_map):
    field, _ = water_map
    start = Point(x=0, y=0)
    end = Point(x=100, y=100)
    raft = Raft(x=0, y=0)
    path_finder = PathFinder(map=field, start=start, end=end, raft=raft)
    path = path_finder.find_shortest_way()
    assert path == [], "Incorrect shortest way!"


def test_end_is_equal_to_start(medium_map):
    field, _ = medium_map
    start = Point(x=0, y=0)
    end = Point(x=0, y=0)
    raft = Raft(x=0, y=0)
    path_finder = PathFinder(map=field, start=start, end=end, raft=raft)
    path = path_finder.find_shortest_way()
    assert path == [], "Incorrect shortest way!"
