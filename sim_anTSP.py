import random
from copy import deepcopy
from math import exp


def energy(matrix, solution):
    total = 0
    for i in range(-1, len(solution) - 1):
        total += matrix[solution[i]][solution[i + 1]]
    return total


def sim_an(matrix, f_t, k, n):
    best_neighbour = [i for i in range(len(matrix[0]))]
    print("Best solution - Random:")
    print(best_neighbour, energy(matrix, best_neighbour))
    neighbour = deepcopy(best_neighbour)
    for i in range(n):
        if i % 100 == 0:
            f_t = (n - i) / n * f_t
        element1 = random.choice(range(len(neighbour)))
        if element1 < len(matrix[0])-1:
            element2 = element1+1
        else:
            element2 = 0
        while element2 == 0:
            element2 = random.choice(range(len(neighbour)))
        neighbour2 = deepcopy(neighbour)
        neighbour2[element1], neighbour2[element2] = neighbour2[element2], neighbour2[element1]
        en1 = energy(matrix, neighbour)
        en2 = energy(matrix, neighbour2)
        p = random.uniform(0, 1)
        if en2 < en1:
            neighbour = deepcopy(neighbour2)
        elif p < exp(((en2 - en1) / (k * f_t)) * (-1)):
            neighbour = deepcopy(neighbour2)
        # if energy(matrix, neighbour) < energy(matrix, best_neighbour):
        #     best_neighbour = neighbour
    print("Best solution - SA:")
    print(neighbour, energy(matrix, neighbour))


# main
mat = [[100000]*8 for i in range(8)]
file = open('D:\\studia\\sem3\\Combinatorial Optimization\\simulated_annealingTSP\\graph.txt', 'r')
for line in file:
    temp = line.split()
    mat[int(temp[0])][int(temp[1])] = int(temp[2])
    mat[int(temp[1])][int(temp[0])] = int(temp[2])
file.close()

sim_an(mat, 10000, 5, 20000)
