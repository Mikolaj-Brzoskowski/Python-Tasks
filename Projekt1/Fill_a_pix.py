import pygad
import numpy as np
import matplotlib.pyplot as plt

board_large = [
    [2,-1,3,-1,3,-1,3,-1,4,5,5,4,-1,-1,0],
    [-1,-1,-1,3,-1,4,-1,4,-1,-1,-1,-1,-1,-1,-1],
    [1,-1,2,1,2,2,3,2,2,2,-1,-1,4,3,-1],
    [-1,-1,3,-1,3,-1,3,-1,0,-1,-1,-1,-1,4,-1],
    [-1,-1,-1,-1,-1,-1,3,-1,-1,-1,-1,5,7,-1,-1],
    [5,-1,-1,7,-1,6,-1,-1,-1,2,-1,-1,-1,-1,-1],
    [-1,-1,5,-1,7,5,5,3,-1,-1,-1,-1,5,4,1],
    [5,-1,-1,7,-1,7,-1,-1,-1,-1,-1,7,-1,-1,-1],
    [-1,-1,7,-1,-1,8,9,-1,-1,9,-1,-1,9,6,-1],
    [5,-1,7,-1,8,-1,7,-1,9,-1,-1,-1,8,7,-1],
    [4,-1,-1,-1,6,-1,-1,-1,6,6,-1,-1,-1,7,5],    
    [-1,-1,6,-1,-1,5,6,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,8,7,-1,-1,7,-1,5,-1,5,8,8,-1,-1,4],
    [-1,8,7,-1,-1,-1,-1,-1,4,-1,8,-1,5,-1,2],
    [-1,-1,-1,-1,3,-1,5,-1,-1,-1,-1,-1,-1,-1,-1]
    ]

board_medium = [
    [-1, 2, 3,-1,-1, 0,-1,-1,-1,-1],
    [-1,-1,-1,-1, 3,-1, 2,-1,-1, 6],
    [-1,-1, 5,-1, 5, 3,-1, 5, 7, 4],
    [-1, 4,-1, 5,-1, 5,-1, 6,-1, 3],
    [-1,-1, 4,-1, 5,-1, 6,-1,-1, 3],
    [-1,-1,-1, 2,-1, 5,-1,-1,-1,-1],
    [ 4,-1, 1,-1,-1,-1, 1, 1,-1,-1],
    [ 4,-1, 1,-1,-1,-1, 1,-1, 4,-1],
    [-1,-1,-1,-1, 6,-1,-1,-1,-1, 4],
    [-1, 4, 4,-1,-1,-1,-1, 4,-1,-1]
]

board_small = [
    [0,-1,4,4,-1],
    [-1,4,-1,6,-1],
    [3,-1,7,6,-1],
    [-1,6,-1,6,5],
    [-1,-1,-1,-1,3]
    ]

gene_space = [0,1]
input = (board_large)

board_small_correct = [
    [1,1,0,0,1],
    [1,1,0,0,1],
    [0,0,1,0,0],
    [1,0,0,0,1],
    [0,0,1,0,0]
]

def fitness_func(solution, solution_idx):
    solution_2d = np.reshape(solution, (len(input),len(input)))
    index_Y = 0
    fitness = 0                
    for y in input:
        index_X = 0
        for x in y:
            if x in range(0,10):
                wrong_squares = check_around(index_Y, index_X, solution_2d, x)
                fitness -= wrong_squares
            index_X+=1
        index_Y+=1
    return fitness

def check_around(index_y, index_x, solution_2d, rule_number):
    black_squares=0
    if (index_y > 0) and (index_y < len(solution_2d)-1) and (index_x > 0) and (index_x < len(solution_2d)-1):
        if solution_2d[index_y-1][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x+1] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x+1] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x+1] == 0:
            black_squares+=1
        return abs(black_squares-rule_number)
    elif (index_y == 0) and (index_x == 0):
        if solution_2d[index_y][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x+1] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x+1] == 0:
            black_squares+=1
        return abs(black_squares-rule_number)
    elif (index_y == 0) and (index_x == len(solution_2d)-1):
        if solution_2d[index_y][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x-1] == 0:
            black_squares+=1
        return abs(black_squares-rule_number)
    elif (index_y == len(solution_2d)-1) and (index_x == 0):
        if solution_2d[index_y][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x+1] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x+1] == 0:
            black_squares+=1
        return abs(black_squares-rule_number)
    elif (index_y == len(solution_2d)-1) and (index_x == len(solution_2d)-1):
        if solution_2d[index_y][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x-1] == 0:
            black_squares+=1
        return abs(black_squares-rule_number)
    elif (index_y == 0):
        if solution_2d[index_y][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x+1] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x+1] == 0:
            black_squares+=1
        return abs(black_squares-rule_number)
    elif (index_y == len(solution_2d)-1):
        if solution_2d[index_y][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x+1] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x+1] == 0:
            black_squares+=1
        return abs(black_squares-rule_number)
    elif (index_x == 0):
        if solution_2d[index_y][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x+1] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x+1] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x+1] == 0:
            black_squares+=1
        return abs(black_squares-rule_number)
    elif (index_x == len(solution_2d)-1):
        if solution_2d[index_y][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y-1][index_x-1] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x] == 0:
            black_squares+=1
        if solution_2d[index_y+1][index_x-1] == 0:
            black_squares+=1
        return abs(black_squares-rule_number)
    

fitness_function = fitness_func

sol_per_pop = 15
num_genes = len(input) * len(input)

num_parents_mating = 7
num_generations = 10000
keep_parents = 3

parent_selection_type="sss"
crossover_type="single_point"
mutation_type="random"
mutation_percent_genes = 100 / num_genes

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
                       mutation_percent_genes=mutation_percent_genes,
                        stop_criteria=["reach_0"]
                    )

ga_instance.run()

solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
generation = ga_instance.best_solution_generation
print("Generation of the best solution= {generation}".format(generation=generation))

#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()
solution_2d = np.reshape(solution, (len(input),len(input)))
plt.imshow(solution_2d, cmap='gray')
plt.show()