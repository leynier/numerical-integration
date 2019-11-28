from roots_legendre import roots_legendre


def gaussian_quadrature(f, a, b, n = 5):
    x, w = roots_legendre(n + 1)
    return 0.5 * (b - a) * sum(w * f(0.5 * (b - a) * x + 0.5 * (b + a)))
