from random import randint

import pytest

from test_2.engine import Triangle, Point, Rectangle, Circle


def random_circle():
    return Circle(
        x=randint(0, 10),
        y=randint(0, 10),
        radius=randint(1, 10),
    )


def random_triangle():
    return Triangle(
        point1=Point(x=randint(0, 10), y=randint(0, 10)),
        point2=Point(x=randint(10, 20), y=randint(10, 20)),
        point3=Point(x=randint(20, 30), y=randint(20, 30)),
    )


def random_rectangle():
    return Rectangle(
        point1=Point(x=randint(0, 10), y=randint(0, 10)),
        point2=Point(x=randint(10, 20), y=randint(10, 20)),
    )


@pytest.fixture(scope="function")
def random_figures():
    def _random_figures(each_qty: int) -> list:
        figures = []
        for figure in (Triangle, Rectangle, Circle):
            for i in range(each_qty):
                if figure == Triangle:
                    figure = random_triangle()
                elif figure == Rectangle:
                    figure = random_rectangle()
                elif figure == Circle:
                    figure = random_circle()
                else:
                    raise AttributeError("There is no such figure!")
                figures.append(figure)
        return figures

    return _random_figures
