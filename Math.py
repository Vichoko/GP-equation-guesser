import sys


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
