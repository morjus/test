import math


def calculate_distance(point_a, point_b) -> float:
    """Calculates distance between two points"""
    return math.sqrt((point_a.x - point_b.x) ** 2 + (point_a.y - point_b.y) ** 2)