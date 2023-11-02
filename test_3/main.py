import random
from collections import deque
from dataclasses import dataclass
from typing import Union


@dataclass
class Point:
    x: int
    y: int

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Land(Point):
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Water(Point):
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


@dataclass
class Raft(Point):
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def up(self) -> None:
        self.y += 1

    def down(self) -> None:
        self.y -= 1

    def left(self) -> None:
        self.x -= 1

    def right(self) -> None:
        self.x += 1

    def move(self, point: Point) -> "Raft":
        x, y = point.x, point.y
        if x > self.x:
            self.right()
        elif x < self.x:
            self.left()
        elif y > self.y:
            self.up()
        elif y < self.y:
            self.down()
        return self


@dataclass
class Map:
    field: dict[str, list] = None
    _land_percent: float = None
    _m: int = None
    _n: int = None

    @property
    def m(self) -> int:
        return self._m

    @property
    def n(self) -> int:
        return self._n

    def get_cell_by_point(self, point: Point) -> Union[Point, None]:
        key = str(hash(point))
        return self.field.get(key, None)

    @classmethod
    def random(cls, m: int, n: int, land_percent: int = 0.3) -> "Map":
        random_map = cls(_land_percent=land_percent, _m=m, _n=n)
        cells_qty = m * n
        land_cells_qty = round(cells_qty * random_map._land_percent)
        water_cells_qty = cells_qty - land_cells_qty
        land_bag = [Land for _ in range(land_cells_qty)]
        water_bag = [Water for _ in range(water_cells_qty)]
        bag = land_bag + water_bag
        random.shuffle(bag)
        random_map.field = dict()
        for x in range(m):
            for y in range(n):
                cell = bag.pop()
                cell = cell(x=x, y=y)
                random_map.field[str(hash(cell))] = cell
        return random_map


@dataclass
class PathFinder:
    map: Map
    raft: Raft
    start: Point
    end: Point

    @classmethod
    def init(cls, m: int, n: int, start: Point, end: Point) -> "PathFinder":
        map = Map().random(m=m, n=n)
        raft = Raft(x=start.x, y=start.y)
        end = end
        start = start
        return cls(map=map, raft=raft, end=end, start=start)

    def get_cell(self, point: Union[Land, Water, Point]) -> Union[Point, None]:
        return self.map.get_cell_by_point(point=point)

    def is_valid_to_move(self, point: Point) -> bool:
        if point == self.end:
            return True
        if isinstance(point, Land):
            return False
        return True

    def find_shortest_way(self) -> list:
        if self.raft == self.end:
            print("You already in the end!")
            return []
        if self.end.x > self.map.m or self.end.y > self.map.n:
            print("No such point on the map!")
            return []

        visited = set()
        queue = deque([(self.start, [])])

        while queue:
            current, path = queue.popleft()
            if current == self.end:
                return path + [current]

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = current.x + dx, current.y + dy
                new_point = Point(new_x, new_y)
                if new_point not in visited:
                    field_point = self.get_cell(point=new_point)
                    if field_point and self.is_valid_to_move(point=field_point):
                        self.raft.move(point=field_point)
                        queue.append((field_point, path + [current]))
                        visited.add(field_point)
                    visited.add(new_point)
        print(f"There is no way from {self.start} to the {self.end}")
        return []
