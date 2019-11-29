from scipy.interpolate import CubicSpline
from gaussian_quadrature import gaussian_quadrature
from utils import print_error


def tabular_form():
    try:
        n = int(input('Insert the number of points of the function to integrate: '))
    except ValueError:
        print_error('Error: The number of points should be a integer.')
    print('Insert the points with the format "x, y":')
    x_points, y_points = [], []
    for _ in range(n):
        try:
            x, y = map(float, input().split(','))
        except ValueError:
            print_error('Error: Incorrect format, the points should be a numbers and the separator should be a comma ",".')
        x_points.append(x)
        y_points.append(y)
    try:
        a, b = map(float, input('Insert the limits with the format "a, b": ').split(','))
    except ValueError:
        print_error('Error: Incorrect format, the limits should be a numbers and the separator should be a comma ",".')
    spline = CubicSpline(x_points, y_points)
    print(gaussian_quadrature(spline, a, b))


def analytical_form():
    pass


if __name__ == "__main__":
    try:
        option = int(input('Insert 1 if the function to be integrated is in the form of a table or 2 if it is in analytical form: ))
        if option != 1 and option != 2:
            print_error('Error: The number of option should be 1 or 2.')
    except ValueError:
        print_error('Error: The number of option should be a integer.')
    if option == 1:
        tabular_form()
    else:
        analytical_form()
