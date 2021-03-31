import random
from itertools import chain
import pandas as pd
import matplotlib.pyplot as plt

stringLen = 20
popSize = 1000
division = -500
probOfMutation = 0.015

df = pd.DataFrame(columns=['Iteration', 'Average'])


# Initialise the population
def initialisePopValues():
    return [[str(random.randint(0, 1)) for i in range(stringLen)] for j in range(popSize)]


# Calculate Fitness (Aiming for all 1s leads to maximum fitness)
def calcFitness(population):
    fitness = []
    for i in range(popSize):
        num = 0
        for j in range(stringLen):
            if population[i][j] == '1':
                num = num + 1

        fitness.append(num)

    return fitness


# Target String Fitness Calculation (Aiming for a specific string for maximum fitness)
def TargetStringCalcFitness(population):
    target_condition = ['0', '1', '1', '0', '0', '0', '1', '1', '0', '1',
                        '0', '0', '1', '0', '1', '0', '1', '0', '0', '1']

    fitness = []
    for i in range(popSize):
        num = 0
        for j in range(stringLen):
            if population[i][j] == target_condition[j]:
                num = num + 1

        fitness.append(num)

    return fitness


# Deceptive Fitness Calculation (If no 1s present, maximum fitness)
def DeceptiveCalcFitness(population):
    fitness = []
    for i in range(popSize):
        num = 0
        for j in range(stringLen):
            if population[i][j] == '1':
                num = num + 1
        if num == 0:
            num = stringLen * 2
        fitness.append(num)

    return fitness


# Sorts and selects the best division of the population
def selection(fitn, k):
    sumOf = 0

    best = sorted(range(len(fitn)), key=lambda i: fitn[i])[division:]

    # Calculates the sum and average fitness among the population
    for j in best:
        sumOf += fitn[j]
    print("--------------------------------------")
    print(f"{k} - Sum of Top {-division}s Fitness = " + str(sumOf))
    average = sumOf / -division
    print(f"{k} - Average of Populations Fitness= " + str(average))

    df.loc[k] = k, average
    return best, average


# Crossover of the top of the population

def crossover(topSelected, pop):
    end = len(topSelected) - 1
    newPop = []

    # The crossover loop is ran for all of the population, until a new population is generated

    for i in range(0, end, 1):

        # A random crosspoint between 1 and 18 is selected in order to split the parents to create a new generation

        crossPoint = (random.randint(1, len(range(stringLen - 2))))
        crossPoint2 = stringLen - crossPoint

        # Person A crosses over with a 2 people, the last person (top mixes with bottom) & a random person

        personA = pop[topSelected[i]]

        peopleB = [pop[topSelected[end - i]]]
        randomPerson = random.sample(range(1, end), 1)
        personB2 = randomPerson.pop(0)
        peopleB.append(pop[topSelected[personB2]])

        # Person A crosses over with both people

        for j in range(len(peopleB)):
            personB = peopleB[j]

            # Parent A and B are then split into their first and second divisions
            sizes = [crossPoint, crossPoint2]
            parA1, parA2 = splitList(sizes, personA)
            parB1, parB2 = splitList(sizes, personB)

            # The children are made by chaining together the first split of one parent and the second split of the other and visa versa
            childA = list(chain(parA1, parB2))
            childB = list(chain(parB1, parA2))
            # They are then added to the new population and returned, bringing the population back up to 1000
            newPop.append(childA)
            newPop.append(childB)

    return newPop


# Split list is used in order to split the parents into 2 separate lists, in order to then be crossed over for the new population
def splitList(sizes, ls):
    par1 = []
    par2 = []

    for s in range(stringLen):
        if s < sizes[0]:
            par1.append(ls[s])
        else:
            par2.append(ls[s])

    return par1, par2


# Decision is used in order to decide if a mutation is to take place
def decision(probability):
    return random.random() < probability


# For the decided random proportion of pop, bit flip mutate
def mutation(person):
    bit = random.randint(0, len(range(stringLen - 1)))

    if person[bit] == "0":
        person[bit] = "1"
    elif person[bit] == "1":
        person[bit] = "0"

    return person


# This function is ran in order to run 1 of 3 of the methods described in main
def method(num):

    initialPop = initialisePopValues()
    avg = 0
    pop = initialPop
    k = 0
    title = ""

    # Here will be loop until convergence
    while avg < 20:

        if num == 1:
            popFit = calcFitness(pop)
            title = "One-max problem"
        elif num == 2:
            popFit = TargetStringCalcFitness(pop)
            title = "Target String Convergence"
        else:
            popFit = DeceptiveCalcFitness(pop)
            title = "Deceptive Landscape"

        popFit.pop(0)
        k += 1
        bestPop, avg = selection(popFit, k)

        pop = crossover(bestPop, pop)

        # Takes each member of the population and mutates with set probability
        for p in range(len(pop)):
            if decision(probOfMutation):
                pop[p] = mutation(pop[p])

    # The Average fitness of the population is graphed over the number of iterations
    df.plot(x='Iteration', y='Average', kind='line')
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    # Type the number 1, 2 and 3 in order to specify what method you want to use
    # Method 1 is the One-max problem
    # Method 2 is Evolving to a target string
    # Method 3 is Deceptive Landscape

    methodNum = 3
    method(methodNum)
