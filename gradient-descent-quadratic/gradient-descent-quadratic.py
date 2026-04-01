def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    x = x0
    while steps:
        x = x - lr * (2*a*x + b)
        steps -= 1

    return x