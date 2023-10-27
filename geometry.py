class Point:

    def __init__(self, ind, x, y):
        """

        :type x: float
        :type y: float

        """
        self.id = ind
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2


class Polygon:

    def __init__(self, points, boundaries):
        self.points = points
        self.boundaries = boundaries

    def get_points(self):
        return self.points

    def get_boundaries(self):
        return self.boundaries
