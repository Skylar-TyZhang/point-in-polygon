from geometry import *


class FileOperations:
    def __init__(self):
        pass

    def read_csv(self, filepath):
        x = []
        y = []
        ind = []
        with open(filepath, 'r') as f:
            for line in f.readlines()[1:]:
                row = line.split(',')
                ind.append(int(row[0]))
                x.append(float(row[1]))
                y.append(float(row[2]))
        return ind, x, y

    def read_polygon(self, file_poly):
        # read a list of vertices coordinate from a csv file
        id_polygon, x_polygon, y_polygon = FileOperations.read_csv(self, file_poly)
        # create a polygon
        poly_points = []
        for i in range(len(id_polygon)):
            poly_points.append(Point(id_polygon[i], x_polygon[i], y_polygon[i]))
        poly_lines = []
        point_a = poly_points[0]
        for point_b in poly_points[1:]:
            poly_lines.append(Line(point_a, point_b))
            point_a = point_b
        poly_lines.append(Line(point_a, poly_points[0]))

        polygon = Polygon(Point(id_polygon, x_polygon, y_polygon), poly_lines)
        return polygon

    # create a polygon object

    def read_input(self, file_input):
        # read a list of input points from a csv file
        id_input, x_input, y_input = FileOperations.read_csv(self, file_input)
        # create a list of point objects
        points_input = []
        for i in range(len(id_input)):
            points_input.append(Point(id_input[i], x_input[i], y_input[i]))
        return points_input

    def write_output(self, output_path, dic):
        with open(output_path, 'w') as f:
            for k, v in dic.items():
                if isinstance(k, int):
                    k += 1

                f.writelines(f'{k} ,{v}\n')

    def get_user_input(self):
        """
        This function is used to get a point coordinate from user
        :return:
        """
        try:
            x_value = float(input('x coordinate: '))
            y_value = float(input('y coordinate: '))
            return x_value, y_value
        except ValueError:
            print('Please input numeric value')
            return FileOperations.get_user_input(self)
