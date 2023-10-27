from categorisation import Categorisation
from file_operation import FileOperations
from mini_boundary_rec import MBR
from plotter import Plotter


def main(polygon_file='polygon.csv', output_file='output.csv'):
    categories = {'id': 'category'}  # store category result in a dictionary
    file_operations = FileOperations()  # create objects
    mbr = MBR()
    categorisation = Categorisation()
    plotter = Plotter()

    # print('read polygon.csv')
    polygon = file_operations.read_polygon(polygon_file)
    # print('read input.csv')
    inputs = file_operations.read_input('input.csv')
    # print('categorize points')
    # print('First find points outside minimum boundary rectangle')

    for i in range(len(inputs)):
        test = inputs[i]  # test each input point
        if not mbr.points_in_mbr(test, polygon):  # the point is out of MBR
            categories[i] = 'outside'

        else:  # loop through all boundaries at given clock-wise oder
            boundaries = polygon.get_boundaries()
            # now apply ray casting algorithm
            count_inter = categorisation.ray_intersections(test, boundaries)
            if count_inter % 2 == 1:
                categories[i] = 'inside'
            elif count_inter % 2 == 0:
                categories[i] = 'outside'
            for boundary in boundaries:
                if categorisation.on_boundary(test, boundary):
                    categories[i] = 'boundary'
                    break

    for key, cate in categories.items():
        try:
            p_x = inputs[key].x
            p_y = inputs[key].y
        except TypeError:  # skip the headline
            # print('This is the headline')
            pass
            continue

        plotter.add_point(p_x, p_y, kind=cate)
        plotter.ray_plotter(polygon, p_x, p_y, kind=cate)

    plotter.add_polygon(polygon.points.x, polygon.points.y)
    plotter.show()

    file_operations.write_output(output_file, categories)


if __name__ == '__main__':
    main()
