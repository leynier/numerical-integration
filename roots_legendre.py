from scipy.special import legendre


def roots_legendre(n):
    p = legendre(n + 1)
    x = legendre(n).roots
    w = 2 * (1 - x ** 2) / ((n + 1) ** 2 * p(x) ** 2)
    return x, w
