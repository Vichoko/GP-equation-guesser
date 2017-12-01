import sys

from matplotlib import pyplot as plt

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


class Analytics:
    """
    Toma datos y prepara figuras para mostrar evolución del fitness vs generaciones
    """

    def __init__(self):
        self.x = []
        self.best_fitness = []
        self.mean_fitness = []

        self.mean_acc = 0
        self.mean_counter = 0
        self.best_acc = sys.float_info.max
        self.local_round = -1

    def dispatch_data(self, roun, fitness):
        """
        Dentro de una ronda, se pasan los datos de cada individuo por este metodo.
        :param roun: Ronda actual
        :param fitness: Fitness de un individuo
        :return: None
        """
        self.local_round = roun
        if fitness <= self.best_acc:
            self.best_acc = fitness

        if fitness <= sys.float_info.max:
            self.mean_acc += fitness
            self.mean_counter += 1

    def close_round(self):
        """
        Se cierra la ronda, en el sentido que no hay más individuos por evaluar.
        Resetea variables de estado.
        :return: None
        """
        if self.local_round == -1:
            raise Exception("Analytics :: no data dispatched for this round")

        print("gen " + str(self.local_round) + " best fitness: " + str(self.best_acc) + " mean fitness: " + str(
            self.mean_acc * 1.0 / self.mean_counter))

        self.x.append(self.local_round)
        self.local_round = -1

        self.best_fitness.append(self.best_acc)
        self.best_acc = sys.float_info.max

        self.mean_fitness.append(self.mean_acc * 1.0 / self.mean_counter)
        self.mean_acc = 0

        self.mean_counter = 0

    def plot(self):
        """
        Dibuja en pantalla los graficos.
        
        :return: None
        """
        plt.figure(1)  # the first figure
        plt.subplot(211)
        plt.title('Fitness Minimo vs Generaciones')  # subplot 211 title

        plt.plot(self.x, self.best_fitness, label='Min_Fitness')
        plt.subplot(212)  # the second subplot in the first figure
        plt.plot(self.x, self.mean_fitness, marker='o', linestyle='--', color='r', label='Mean_Fitness')
        plt.title('Fitness Medio vs Generaciones')  # subplot 211 title
        plt.show()
