import math
import random
import turtle
import pytest

from .engine import (
    Point,
    Circle,
    Rectangle,
    Triangle,
    Engine2D,
)


class TestPoint:
    @pytest.mark.parametrize("x, y", [(-1, -1), (0, 0), (1, 1), (-1, 1)])
    def test_point_init(self, x, y):
        point = Point(x=x, y=y)
        assert point.x == x, f"Incorrect x! Expected {x}, got {point.x}"
        assert point.y == y, f"Incorrect y! Expected {y}, got {point.y}"

    def test_point_repr(self):
        x, y = (-1, 1)
        point = Point(x=x, y=y)
        expected_repr = f"{(x, y)}"
        assert (
            repr(point) == expected_repr
        ), f"Incorrect representation! Expected: {expected_repr}, got: {repr(point)}"


class TestCircle:
    @pytest.mark.parametrize(
        "x, y, radius", [(-1, -1, 1), (0, 0, 2), (1, 1, 3), (-1, 1, 5)]
    )
    def test_circle_init(self, x, y, radius):
        circle = Circle(x=x, y=y, radius=radius)
        assert circle.x == x, f"Incorrect x! Expected {x}, got {circle.x}"
        assert circle.y == y, f"Incorrect y! Expected {y}, got {circle.y}"
        assert (
            circle.radius == radius
        ), f"Incorrect y! Expected {y}, got {circle.radius}"

    @pytest.mark.parametrize("color", ["black", (41, 41, 253), None])
    def test_circle_repr(self, color):
        x = random.randint(1, 10)
        y = random.randint(10, 20)
        radius = random.randint(20, 30)
        circle = Circle(
            x=x,
            y=y,
            radius=radius,
            color=color,
        )
        expected_repr = f"Circle: {(x, y)} with radius {radius}"
        if color:
            expected_repr = expected_repr + f" and color={color}"

        assert (
            repr(circle) == expected_repr
        ), f"Incorrect representation! Expected: {expected_repr}, got: {repr(circle)}"

    @pytest.mark.parametrize("incorrect_radius", [0, -1])
    def test_incorrect_circle(self, incorrect_radius):
        with pytest.raises(AttributeError) as excinfo:
            Circle(
                x=random.randint(1, 10),
                y=random.randint(10, 20),
                radius=incorrect_radius,
            )
            assert (
                excinfo.value == f"Wrong circle radius: {incorrect_radius}!"
            ), "Circle is right!"


class TestRectangle:
    def test_rectangle_init(self):
        p1 = Point(x=random.randint(0, 10), y=random.randint(0, 10))
        p2 = Point(x=random.randint(10, 20), y=random.randint(10, 20))
        rectangle = Rectangle(point1=p1, point2=p2)

        length = abs(p2.x - p1.x)
        height = abs(p2.y - p1.y)

        for p, point in zip((p1, p2), (rectangle.point1, rectangle.point2)):
            assert p == point, "Incorrect init!"

        assert (
            rectangle.length == length
        ), f"Incorrect length: {rectangle.length}, expected {length}"
        assert (
            rectangle.height == height
        ), f"Incorrect height: {rectangle.height}, expected {height}"

    @pytest.mark.parametrize("color", ["blue", (40, 19, 145), None])
    def test_rectangle_repr(self, color):
        p1 = Point(x=random.randint(0, 10), y=random.randint(0, 10))
        p2 = Point(x=random.randint(10, 20), y=random.randint(10, 20))
        rectangle = Rectangle(point1=p1, point2=p2, color=color)

        length = abs(p2.x - p1.x)
        height = abs(p2.y - p1.y)

        expected_repr = (
            f"Rectangle: {(p1, p2)} " f"with length={length} " f"and height={height} "
        )
        if color:
            expected_repr = expected_repr + f" and color={color}"

        assert (
            repr(rectangle) == expected_repr
        ), f"Incorrect representation! Expected: {expected_repr}, got: {repr(rectangle)}"

    def test_incorrect_rectangle(self):
        p1 = Point(x=random.randint(0, 0), y=random.randint(0, 0))
        p2 = Point(x=random.randint(0, 0), y=random.randint(10, 20))
        with pytest.raises(AttributeError) as excinfo:
            Rectangle(point1=p1, point2=p2)
            assert (
                excinfo.value == "Wrong rectangle coordinates!"
            ), "Rectangle is correct!"


class TestTriangle:
    def test_triangle_init(self):
        p1 = Point(x=random.randint(0, 10), y=random.randint(0, 10))
        p2 = Point(x=random.randint(10, 20), y=random.randint(10, 20))
        p3 = Point(x=random.randint(20, 30), y=random.randint(20, 30))
        triangle = Triangle(
            point1=p1,
            point2=p2,
            point3=p3,
        )
        for p, point in zip(
            (p1, p2, p3), (triangle.point1, triangle.point2, triangle.point3)
        ):
            assert p == point, "Incorrect init!"

        a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
        b = math.sqrt((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2)
        c = math.sqrt((p3.x - p1.x) ** 2 + (p3.y - p1.y) ** 2)

        assert triangle.a == a, f"Incorrect edge a: {triangle.a}, expected {a}"
        assert triangle.b == b, f"Incorrect edge b: {triangle.b}, expected {b}"
        assert triangle.c == c, f"Incorrect edge c: {triangle.c}, expected {c}"

    @pytest.mark.parametrize("color", ["green", (40, 19, 145), None])
    def test_triangle_repr(self, color):
        p1 = Point(x=random.randint(0, 10), y=random.randint(0, 10))
        p2 = Point(x=random.randint(10, 20), y=random.randint(10, 20))
        p3 = Point(x=random.randint(20, 30), y=random.randint(20, 30))
        triangle = Triangle(
            point1=p1,
            point2=p2,
            point3=p3,
            color=color,
        )
        a = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
        b = math.sqrt((p2.x - p3.x) ** 2 + (p2.y - p3.y) ** 2)
        c = math.sqrt((p3.x - p1.x) ** 2 + (p3.y - p1.y) ** 2)

        expected_repr = (
            f"Triangle: {(p1, p2, p3)} "
            f"with edge1={abs(a)} "
            f"and edge2={abs(b)} "
            f"and edge3={abs(c)}"
        )
        if color:
            expected_repr = expected_repr + f" and color={color}"

        assert (
            repr(triangle) == expected_repr
        ), f"Incorrect representation! Expected: {expected_repr}, got: {repr(triangle)}"

    def test_incorrect_triangle(self):
        p1 = Point(x=random.randint(0, 10), y=random.randint(0, 10))
        p2 = Point(x=random.randint(10, 10), y=random.randint(10, 10))
        p3 = Point(x=random.randint(10, 10), y=random.randint(10, 10))
        with pytest.raises(AttributeError) as excinfo:
            Triangle(
                point1=p1,
                point2=p2,
                point3=p3,
            )
            assert (
                excinfo.value == "Wrong triangle coordinates!"
            ), "Triangle is correct!"


class TestEngine:
    @pytest.mark.parametrize("color", ["black", "#285078", (1, 1, 1)])
    def test_change_color(self, color):
        engine = Engine2D()
        assert engine.color is None, "After the initiation, the color came out!"
        engine.change_color(color=color)
        assert engine.color == color, "The color hasn't changed!"

    def test_figures_empty_after_drawing(self, random_figures):
        random_figures = random_figures(each_qty=1)
        engine = Engine2D()
        for figure in random_figures:
            engine.append_figure(figure=figure)
        engine.draw()
        assert not engine.figures, "The figures have not been removed!"

    @pytest.mark.parametrize("incorrect_color", [(256, 256, 256), (-1, -1, -1)])
    def test_change_to_incorrect_color_1(self, incorrect_color):
        engine = Engine2D()
        with pytest.raises(turtle.TurtleGraphicsError) as excinfo:
            engine.change_color(color=incorrect_color)
            assert str(excinfo.value) == f"bad color sequence: {incorrect_color}"

    @pytest.mark.parametrize("incorrect_color", [None])
    def test_change_to_incorrect_color_2(self, incorrect_color):
        engine = Engine2D()
        with pytest.raises(TypeError) as excinfo:
            engine.change_color(color=incorrect_color)
        assert str(excinfo.value) == "object of type 'NoneType' has no len()"
