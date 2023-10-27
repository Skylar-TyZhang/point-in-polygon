from categorisation import Categorisation
from plotter import Plotter
from file_operation import FileOperations
from geometry import Point
from mini_boundary_rec import MBR


def main():
    plotter = Plotter()
    file_operations = FileOperations()
    mbr = MBR()
    categorisation = Categorisation()
    category = None
    print('read polygon.csv')
    polygon = file_operations.read_polygon('polygon.csv')
    print('Insert point information')
    x, y = file_operations.get_user_input()
    test = Point('user input', x, y)
    if not mbr.points_in_mbr(test, polygon):  # the point is out of MBR
        print('outside')
        category = 'outside'
    else:
        boundaries = polygon.get_boundaries()
        count_inter = categorisation.ray_intersections(test, boundaries)
        if count_inter % 2 == 1:
            print('inside')
            category = 'inside'
        elif count_inter % 2 == 0:
            print('outside')
            category = 'outside'
        for boundary in boundaries:
            if categorisation.on_boundary(test, boundary):
                print('boundary')
                category = 'boundary'
                break

    print('plot polygon and point')
    plotter.add_point(x, y, category)
    plotter.add_polygon(polygon.points.x, polygon.points.y)
    plotter.ray_plotter(polygon, x, y, kind=category)
    plotter.show()


if __name__ == '__main__':
    main()
