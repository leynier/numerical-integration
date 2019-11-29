from scipy import array, ndarray
from scipy.interpolate import CubicSpline
from sympy import sympify, SympifyError
from gaussian_quadrature import gaussian_quadrature
from utils import print_error


def get_limits():
    try:
        a, b = map(float, input('Insert the limits with the format "a, b": ').split(','))
    except ValueError:
        print_error('Error: Incorrect format, the limits should be a numbers and the separator should be a comma ",".')
    return a, b


def get_tabular_form_input():
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
    return x_points, y_points


def get_tabular_form():
    x_points, y_points = get_tabular_form_input()
    function = CubicSpline(x_points, y_points)
    return function


def get_analytical_form():
    try:
        function = sympify(input('Insert the analytical form of the function: '))
    except SympifyError:
        print_error('Error: It is not a recognizable function')
    return lambda arg: array([function.evalf(subs={'x': i}) for i in arg]) if isinstance(arg, (tuple, list, ndarray)) else function.evalf(subs={'x': arg})


if __name__ == "__main__":
    try:
        option = int(input('Insert 1 if the function to be integrated is in the form of a table or 2 if it is in analytical form: '))
        if option != 1 and option != 2:
            print_error('Error: The number of option should be 1 or 2.')
    except ValueError:
        print_error('Error: The number of option should be a integer.')
    function = get_tabular_form() if option == 1 else get_analytical_form()
    a, b = get_limits()
    print(gaussian_quadrature(function, a, b))
