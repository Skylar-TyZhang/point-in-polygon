class Categorisation:
    def __init__(self):
        pass

    def on_boundary(self, p_test, edge):
        """
        Tell if the test point is on boundary of the polygon
        :param p_test: the test point
        :param edge: the boundary
        :return: True if the point is on boundary, False if not.
        """
        p_1 = edge.point_1
        p_2 = edge.point_2
        # First make sure the test point is in MBR set by boundary vertices
        if min(p_1.x, p_2.x) <= p_test.x <= max(p_1.x, p_2.x) and min(p_1.y, p_2.y) <= p_test.y <= max(p_1.y, p_2.y):
            # if p_1.x == p_2.x:  # The boundary is vertical
            #    return True
            try:
                m_slope = (p_1.y - p_2.y) / (p_1.x - p_2.x)
                if p_test.y == m_slope * (p_test.x - p_2.x) + p_2.y:
                    return True
            except ZeroDivisionError:  # The boundary is vertical
                return True
            # Reference of the error handling function :http://philliplemons.com/posts/ray-casting-algorithm

    def ray_intersections(self, p_test, edges):
        """
        The function is designed to count
        intersections of ray initiated by the test point
        and boundaries of polygon
        :param p_test: point to test
        :param edges: boundaries of the polygon
        :return: number of intersections
        """

        count = 0
        l_previous = edges[0]
        for ind, l_current in enumerate(edges):  # loop through all edges in clock-wise order
            p_a = l_previous.point_1
            p_b = l_previous.point_2
            p_c = l_current.point_1
            p_d = l_current.point_2  # p_a and p_d are 2 vertices that ray does not cross
            l_previous = l_current

            # set ray as a horizontal right forward line
            if p_c.y != p_d.y and p_test.x < max(p_c.x, p_d.x):  # the current edge is not parallel to the ray
                # make sure that the ray is not at the same height as vertex
                # and that the test point is on the left side of edge
                if min(p_c.y, p_d.y) < p_test.y < max(p_c.y,
                                                      p_d.y):  # The ray vertically between the vertices of the edge
                    count += 1  # intersects once

                elif p_test.y == p_c.y and p_test.x < p_c.x:  # the ray crosses a vertex of a not horizontal edge

                    if (p_a.y - p_test.y) * (p_d.y - p_test.y) < 0:  # 2 non-vertex points are one above and on below
                        count += 1

                    elif (p_a.y - p_test.y) * (
                            p_d.y - p_test.y) > 0:  # 2 non vertex points are on the same side of the point
                        count += 0

            else:
                # The edge is parallel to the ray
                if p_test.y == p_c.y == p_d.y:  # The ray will cross a horizontal edge,skip this edge
                    if ind < len(edges) - 1:
                        l_next = edges[ind + 1]  # get the next edge, which is not horizontal
                    else:
                        l_next = edges[-1]
                    p_e = l_next.point_2
                    if (p_a.y - p_test.y) * (
                            p_e.y - p_test.y) > 0:  # non-horizontal edges are on the same side of the horizontal one
                        count += 0  # do not count
                    elif (p_a.y - p_test.y) * (
                            p_e.y - p_test.y) < 0:  # non-horizontal edges are on different sides of the horizontal one
                        count += 1
        return count
