import pygad
import numpy

maze = [   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
            [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
            [0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 3, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#definiujemy parametry chromosomu
#geny to liczby: 0 lub 1
gene_space = [0, 1, 2, 3]

#definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    length = len(solution)
    start_1 = 1
    start_2 = 1
    end = maze[-2][-2]
    pointer = maze[start_1][start_2]
    for i in solution:
        match i:
            case 0:
                start_2 += 1
                pointer = maze[start_1][start_2]
            case 1:
                start_1 += 1
                pointer = maze[start_1][start_2]
            case 2:
                start_2 -= 1
                pointer = maze[start_1][start_2]
            case 3:
                start_1 -= 1
                pointer = maze[start_1][start_2]
        if pointer == 0:
            return -1
        elif pointer == 1:
            length -= 1  
        elif pointer == end:
            return length
    return 0

fitness_function = fitness_func

#ile chromsomów w populacji
#ile genow ma chromosom

sol_per_pop = 30
num_genes = 30

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 15
num_generations = 2000
keep_parents = 2

parent_selection_type = "sss"

crossover_type = "single_point"

mutation_type = "random"
mutation_percent_genes = 4

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_function,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes
                       )

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Steps left in the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
generation = ga_instance.best_solution_generation
print("Generation of the best solution = {generation}".format(generation=generation))

ga_instance.plot_fitness()