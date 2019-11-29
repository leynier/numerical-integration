from scipy.interpolate import CubicSpline
from gaussian_quadrature import gaussian_quadrature
from utils import print_error


if __name__ == "__main__":
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
