from collections import OrderedDict

import matplotlib
import matplotlib.pyplot as plt

# if plotting does not work comment the following line
matplotlib.use('TkAgg')


class Plotter:

    def __init__(self):
        plt.figure()

    def add_polygon(self, xs, ys):
        plt.fill(xs, ys, 'lightgray', label='Polygon')

    def add_point(self, x, y, kind=None):
        if kind == 'outside':
            plt.plot(x, y, 'ro', label='Outside')

        elif kind == 'boundary':
            plt.plot(x, y, 'bo', label='Boundary')
        elif kind == 'inside':
            plt.plot(x, y, 'go', label='Inside')
        else:
            plt.plot(x, y, 'ko', label='Unclassified')

    def show(self):
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys(), fontsize=8, loc='upper left')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')

        plt.title('Result of Point in Polygon categorisation')
        plt.show()

    def ray_plotter(self, polygon_obj, x_, y_, kind=None):
        """
        This function is to plot ray from test points inside the
        minimum boundary rectangle.
        :param polygon_obj: get polygon MBR
        :param x_:X coordinate of test point
        :param y_: Y coordinate of test point
        :param kind: Point category
        :return:
        """
        poly = polygon_obj.points
        x_max = max(poly.x)
        y_max = max(poly.y)
        x_min = min(poly.x)
        y_min = min(poly.y)
        if x_min <= x_ <= x_max and y_min <= y_ <= y_max:

            if kind == 'outside':

                plt.plot([x_, x_max + 1], [y_, y_], linestyle=':', color='r', label='Ray from outside point')


            elif kind == 'inside':
                plt.plot([x_, x_max + 1], [y_, y_], linestyle=':', color='g', label='Ray from inside point')

    def save_fig(self, fig_path):
        plt.savefig(fig_path)
