import random
from itertools import chain

import numpy as np

stringLen = 20
popSize = 100
fitness = [0]
division = -20
probOfMutation = 0.2


# Initialise the population
def initialisePopValues():
    return [[str(random.randint(0, 1)) for i in range(stringLen)] for j in range(popSize)]


# Calculate Fitness
def calcFitness():
    for i in range(popSize):

        num = 0
        for j in range(stringLen):
            if currPop[i][j] == '1':
                num = num + 1

        fitness.append(num)
    return fitness


def selection():
    sumOf = 0
    best = sorted(range(len(fitness)), key=lambda i: fitness[i])[division:]

    for j in best:
        sumOf += fitness[j]

    print("Sum of Top 20s Fitness = " + str(sumOf))
    avg = sumOf / -division
    print("Average of Populations Fitness= " + str(avg))
    return best


# Crossover of the top twenty of the population

def crossover(pop):
    end = len(bestPop) - 1

    newPop = []

    # Person A crosses over with a list of 5 people

    for i in range(0, end, 2):
        crossPoint = (random.randint(1, len(range(stringLen - 2))))
        crossPoint2 = stringLen - crossPoint

        personA = pop[bestPop[i]]

        peopleB = random.sample(range(1, 20), 5)

        for j in range(len(peopleB)):
            personB = pop[bestPop[peopleB[j]]]

            sizes = [crossPoint, crossPoint2]
            parA1, parA2 = splitList(sizes, personA)
            parB1, parB2 = splitList(sizes, personB)

            childA = list(chain(parA1, parB2))
            childB = list(chain(parB1, parA2))
            newPop.append(childA)
            newPop.append(childB)

    pop = newPop
    return pop


def splitList(sizes, list):
    par1 = []
    par2 = []

    for s in range(-division):
        if s < sizes[0]:
            par1.append(list[s])
        else:
            par2.append(list[s])

    return par1, par2


def decision(probability):
    return random.random() < probability


# For the decided random proportion of pop, bit flip mutate
def mutation(person):
    bit = random.randint(0, len(range(stringLen - 1)))
    person[bit] = int(not person[bit])
    return person


if __name__ == '__main__':
    currPop = initialisePopValues()
    avg = 0
    # Here will be loop until convergence
    while avg < 350:
        fitness = calcFitness()

        fitness.pop(0)
        bestPop = selection()

        perfect_condition = ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                             '1', '1', '1', '1', '1', '1', '1', '1', '1', '1']
        pop = crossover(currPop)

        # Takes each member of the population and mutates with set probability
        for i in range(len(pop)):
            if decision(probOfMutation):
                pop[i] = mutation(pop[i])

