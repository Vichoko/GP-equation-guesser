import sys
from random import *

import numpy as np

from AST import Ast
from Global import POPULATION_SIZE, CROSSOVER_CHANCE, SEX_CHANCE, MUTATION_CHANCE, TOURNAMENT_K, NUMBER_OF_OPERATIONS, \
    MIN_ACCEPTABLE_ERROR


def tournament_select(pop, k):
    """
    Elije el mejor candidato de la populacion entre k individuos.
    :param pop: Arreglo de poblacion
    :param k: Cantidad de intentos
    :return: Mejor candidato
    """
    best_ast = None
    best_fitness = sys.float_info.max
    while k > 0:
        random_ast = choice(pop)
        fitness = random_ast.fitness
        random_ast.count_nodes()
        if random_ast.binop_count >= NUMBER_OF_OPERATIONS * 5:
            # workaround for AST Size control
            # print("dropped in tournament")
            continue
        if fitness <= best_fitness:
            best_fitness = random_ast.fitness
            best_ast = random_ast
        k -= 1
    if best_ast is None:
        # workaround when every choice is better than best
        best_ast = choice(pop)
    return best_ast


def evolution_loop():
    """
    Ejecuta evolucion de AST. Termina cuando exista un individuo con error < MIN_ACCEPTABLE_ERROR.
    
    :return: None
    """
    population = []
    for i in range(POPULATION_SIZE):
        population.append(Ast.random_generate())
    gen_counter = 0
    run = True
    perfect_individual = None
    print("Starting Evolution")
    while run:
        gen_counter += 1
        # calculate fitness
        best_fitness = sys.float_info.max
        best_individual = None
        for ast in population:
            fitness = ast.get_fitness()
            if fitness <= MIN_ACCEPTABLE_ERROR:
                perfect_individual = ast
                run = False
                break
            if fitness < best_fitness:
                best_fitness = fitness
                best_individual = ast
        if not run:
            break
        print("gen " + str(gen_counter) + " best fitness: " + str(best_fitness))
        # reproduce & mutate
        offspring = []
        while len(offspring) < POPULATION_SIZE:
            # pick parents
            dad = tournament_select(population, TOURNAMENT_K)
            mom = tournament_select(population, TOURNAMENT_K)
            # evaluate sex chance
            if np.random.random_sample() >= SEX_CHANCE:
                continue

            # evaluate crossover chace
            if np.random.random_sample() <= CROSSOVER_CHANCE:
                son = Ast.from_parents(dad, mom)
            else:
                son = dad.copy() if random() >= 0.5 else mom.copy()
            # evaluate mutation chance
            if np.random.random_sample() <= MUTATION_CHANCE:
                son.mutate()
            # append son
            offspring.append(son)
        # after offspring generation, replace previous population
        population = offspring
    print(" Evolution ended")
    print(" Best individual is: ")
    perfect_individual.print()
    print("Best Fitness: " + str(perfect_individual.fitness))


if __name__ == "__main__":
    evolution_loop()
