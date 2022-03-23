import pygad
import numpy

S = [   [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,2,0,0,1,0,0,0,1,0,0,1],
        [1,1,1,0,0,0,1,0,1,1,0,1],
        [1,0,0,0,1,0,1,0,0,0,0,1],
        [1,0,1,0,1,1,0,0,1,1,0,1],
        [1,0,0,1,1,0,0,0,1,0,0,1],
        [1,0,0,0,0,0,1,0,0,0,1,1]]

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = {'low': 0.0, 'high': 1.0}

#definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    sum = endurance(*solution)
    fitness = sum
    return fitness

fitness_function = fitness_func