# Math Constants
MAX_NUMBER = 5.0
MIN_NUMBER = -5.0
MAX_DEPTH = 5
MIN_ACCEPTABLE_ERROR = 0.1
DELTA = 0.1

# Evolution parameters
POPULATION_SIZE = 1000
CROSSOVER_CHANCE = 0.5
SEX_CHANCE = 0.8
MUTATION_CHANCE = 0.1
TOURNAMENT_K = 2

# Target expression
NUMBER_OF_OPERATIONS = 8  # change as you change the polynomial


def polynomial(x):
    """
    Polinomio ideal al que se quiere converger.
    
    :param x: Valor de evaluacion de x.
    :return: Valor resultado.
    """
    return 3 * x ** 2 + 2 * x + 3 + x ** 3
