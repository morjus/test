import abc
from dataclasses import dataclass, field
from typing import Iterable, List, Union

from test_2.utils import calculate_distance
import turtle

from test_2.draw_helper import penup_always


@dataclass
class Point:
    x: int
    y: int

    def __repr__(self):
        return repr((self.x, self.y))


@dataclass
class TriangleBase(abc.ABC):
    point1: Point
    point2: Point
    point3: Point

    a: float = field(init=False)
    b: float = field(init=False)
    c: float = field(init=False)

    def __post_init__(self):
        if not self.is_valid_triangle():
            raise AttributeError("Wrong triangle coordinates!")

    def is_valid_triangle(self) -> bool:
        a = calculate_distance(self.point1, self.point2)
        b = calculate_distance(self.point2, self.point3)
        c = calculate_distance(self.point3, self.point1)
        self.a, self.b, self.c = a, b, c
        return a + b > c and b + c > a and c + a > b

    @abc.abstractmethod
    def draw(self):
        """Draws a figure"""
        raise NotImplementedError("The method should be implemented!")


@dataclass
class RectangleBase(abc.ABC):
    point1: Point
    point2: Point

    length: float = field(init=False)
    height: float = field(init=False)

    def __post_init__(self):
        if not self.is_valid_rectangle():
            raise AttributeError("Wrong rectangle coordinates!")
        self.length = abs(self.point2.x - self.point1.x)
        self.height = abs(self.point2.y - self.point1.y)

    def is_valid_rectangle(self) -> bool:
        return (self.point1.x != self.point2.x) and (self.point1.y != self.point2.y)

    @abc.abstractmethod
    def draw(self):
        """Draws a figure"""
        raise NotImplementedError("The method should be implemented!")


@dataclass
class Circle(Point):
    radius: float
    color: str = None
    canvas: turtle.Turtle = None

    def __post_init__(self):
        if not self.is_valid_circle():
            raise AttributeError(f"Wrong circle radius: {self.radius}!")

    def is_valid_circle(self) -> bool:
        return self.radius > 0

    def __repr__(self) -> str:
        string = (
            f"{self.__class__.__name__}: {(self.x, self.y)} "
            f"with radius {self.radius}"
        )
        if self.color:
            string = string + f" and color={self.color}"
        return string

    @penup_always
    def draw(self) -> "Circle":
        if not self.canvas:
            raise AttributeError("There is no canvas to draw!")
        print(f"Drawing {self}")
        self.canvas.goto(x=self.x, y=self.y)
        self.canvas.pendown()
        self.canvas.circle(radius=self.radius)
        return self


@dataclass
class Rectangle(RectangleBase):
    color: str = None
    canvas: turtle.Turtle = None

    def __repr__(self) -> str:
        string = (
            f"{self.__class__.__name__}: {(self.point1, self.point2)} "
            f"with length={abs(self.length)} "
            f"and height={abs(self.height)} "
        )
        if self.color:
            string = string + f" and color={self.color}"
        return string

    @penup_always
    def draw(self) -> "Rectangle":
        if not self.canvas:
            raise AttributeError("There is no canvas to draw!")
        print(f"Drawing {self}")
        angle = 90
        self.canvas.goto(x=self.point1.x, y=self.point1.y)
        self.canvas.pendown()
        self.canvas.forward(self.length)
        self.canvas.left(angle)
        self.canvas.forward(self.height)
        self.canvas.left(angle)
        self.canvas.forward(self.length)
        self.canvas.left(angle)
        self.canvas.forward(self.height)
        return self


@dataclass
class Triangle(TriangleBase):
    color: str = None
    canvas: turtle.Turtle = None

    def __repr__(self) -> str:
        string = (
            f"{self.__class__.__name__}: {(self.point1, self.point2, self.point3)} "
            f"with edge1={abs(self.a)} "
            f"and edge2={abs(self.b)} "
            f"and edge3={abs(self.c)}"
        )
        if self.color:
            string = string + f" and color={self.color}"
        return string

    @penup_always
    def draw(self) -> "Triangle":
        if not self.canvas:
            raise AttributeError("There is no canvas to draw!")
        print(f"Drawing {self}")

        self.canvas.goto(x=self.point1.x, y=self.point1.y)
        self.canvas.pendown()
        self.canvas.goto(x=self.point2.x, y=self.point2.y)
        self.canvas.goto(x=self.point3.x, y=self.point3.y)
        self.canvas.goto(x=self.point1.x, y=self.point1.y)
        return self


@dataclass
class Engine2D:
    figures: List[Union[Circle, Triangle, Rectangle]] = field(default_factory=list)
    color: Union[str, Iterable[Union[str, int]]] = None
    _canvas: turtle.Turtle = turtle.Turtle()

    def append_figure(self, figure: Union[Circle, Triangle, Rectangle]) -> list:
        self.figures.append(figure)
        return self.figures

    def change_color(self, color: Union[str, Iterable[Union[str, int]]]) -> None:
        self.color = color
        self._canvas.color(color)

    def draw(self) -> None:
        if not self.figures:
            raise AttributeError("There is no figures to draw!")
        for figure in self.figures:
            if self.color:
                figure.color = self.color
            figure.canvas = self._canvas
            figure.draw()
        self.figures = []
