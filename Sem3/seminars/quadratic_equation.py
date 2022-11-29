def q_equation_solver(a, b, c):
    """
    Solving a quadratic equation
    :param a: quadratic coefficient
    :param b: linear coefficient
    :param c: free coefficient
    :return: answer
    """
    D = b ** 2 - 4 * a * c

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        return "x1 = {:.3f}, x2 = {:.3f}".format(x1, x2)

    elif D == 0:
        x = -b / (2 * a)
        return "x = {:.3f}".format(x)

    else:
        return "no solutions"


print(q_equation_solver(4, 3, -10))
