class MBR:
    def __init__(self):
        pass

    def points_in_mbr(self, p, polygon_obj):
        """
        :param p: input point to test
        :param polygon_obj:  polygon object
        :return: False if input point is outside MBR
        """
        poly = polygon_obj.points
        x_max = max(poly.x)
        y_max = max(poly.y)
        x_min = min(poly.x)
        y_min = min(poly.y)

        # test point
        if x_min <= p.x <= x_max and y_min <= p.y <= y_max:
            return True

        else:
            return False
