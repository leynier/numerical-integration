from roots_legendre import roots_legendre


def gaussian_quadrature(f, a, b, n = 5):
    """
    Compute a definite integral using fixed-order Gaussian quadrature.

    Integrate `f` from `a` to `b` using Gaussian quadrature of
    order `n`.

    Parameters
    ----------
    f : callable
        A Python function or method to integrate.
    a : float
        Lower limit of integration.
    b : float
        Upper limit of integration.
    n : int, optional
        Order of quadrature integration. Default is 5.

    Returns
    -------
    val : float
        Gaussian quadrature approximation to the integral
    """
    x, w = roots_legendre(n + 1)
    return 0.5 * (b - a) * sum(w * f(0.5 * (b - a) * x + 0.5 * (b + a)))
