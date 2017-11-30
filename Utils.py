import sys

from Global import MAX_NUMBER, MIN_NUMBER, DELTA, polynomial


def sumar_num(val1, val2):
    """sumar_num :: Float x Float -> Float
    Suma los 2 valores solo si son Float"""
    if val1.__class__.__name__ == 'float' and val2.__class__.__name__ == 'float':
        res = val1 + val2
        return res
    else:
        raise TypeError("sumar_num :: Se deben sumar valores que sean float")


def restar_num(val1, val2):
    """restar_num :: Float x Float -> Float
    Resta los 2 valores solo si son Float"""

    if val1.__class__.__name__ == 'float' and val2.__class__.__name__ == 'float':
        res = val1 - val2
        return res
    else:
        print(val1.__class__.__name__)
        print(val2.__class__.__name__)
        raise TypeError("restar_num :: Se deben restar valores que sean float")


def dividir_num(val1, val2):
    """restar_num :: Float x Float -> Float
    Divide los 2 valores solo si son Float"""

    if val1.__class__.__name__ == 'float' and val2.__class__.__name__ == 'float':
        if val2 != 0:
            res = val1 / val2
        else:
            res = sys.float_info.max
        return res
    else:
        print(val1.__class__.__name__)
        print(val2.__class__.__name__)
        raise TypeError("dividir_num :: Se deben dividir valores que sean float")


def multip_num(val1, val2):
    """restar_num :: Float x Float -> Float
    Multiplica los 2 valores solo si son Float"""

    if val1.__class__.__name__ == 'float' and val2.__class__.__name__ == 'float':
        res = val1 * val2
        return res
    else:
        print(val1.__class__.__name__)
        print(val2.__class__.__name__)
        raise TypeError("multip_num :: Se deben multiplicar valores que sean float")


def fitness_fun(ast):
    # generate test set
    length = (MAX_NUMBER - MIN_NUMBER) / DELTA
    sqrd_errors = 0
    # ast.print()

    for i in range(int(length)):
        x = MIN_NUMBER + i * DELTA
        if x == 0:
            continue
        expected_y = polynomial(x)
        actual_y = ast.evaluate(x)
        # print("x is " + str(x) + " expected: " + str(expected_y) + " actual: " + str(actual_y))
        try:
            sqrd_errors += (expected_y - actual_y) ** 2
        except OverflowError:
            # print("overflow")
            sqrd_errors += sys.float_info.max
    mean_sqrt_error = sqrd_errors / length

    # print("    fitness is " + str(mean_sqrt_error))
    return mean_sqrt_error
