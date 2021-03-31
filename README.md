# Genetic-Algorithms

 ## One Max problem
I implemented the OneMax class across 8 functions:

•	initialisePopValues

•	calcFitness, TargetStringCalcFitness, DeceptiveCalcFitness

•	selection

•	crossover

•	mutation

•	splitList

•	decision

•	method

Method was called from the main function with an argument of either 1, 2 or 3, 1 being the original One-Max problem, 2 being Evolving to a target string, and 3 being Deceptive Landscape.


Firstly, the population is initialised by having all of the population randomly set to a list of 1s & 0s. From here we enter the loop which runs until the average fitness is 20 (20 being where the entire populations average has reached the maximum point i.e., all lists having all ones / all lists being the target / all lists reaching the maximum).


We then calculate the fitness in 3 different functions depending on which method you have chosen (calcFitness, TargetStringCalcFitness, DeceptiveCalcFitness).


From there the populations fitness is then inputted into the selection function which sorts and selects the best division of the population. The Sum of fitness and average is then calculated and outputted to the console and to the dataframe for the graph. 


From here the best selection of the sorted population is then sent to the Crossover function. The crossover is ran for the entire population and takes a randomised Crosspoint between 1 & 18 and finds and opposite length as well in order to divide the list of the 2 parents in the splitList function. Then the output from this is taken as two lists, parent part 1 and parent part 2, with the size defined by the crosspoint, and part 1 of parent A is then chained together with part 2 of parent B and vice versa in order to crossover the population and generate a new one.

From here, using the decision function to use the assigned probability of mutation, we run through a loop of the population and mutate according to that probability. I used a single random bit flip.

 Results:
From the following graphs we can see a steady growth with large portions of the chart plateauing at each increment as we see the population amalgamating towards a newly discovered increase to fitness. For the One-max problem we saw this primarily towards the end as the entire population must reach a perfect fitness of 20 in order to reach the complete status.

![OneMax](https://i.imgur.com/xXkX8zv.png)
              
      Figure 1: Graph of One-Max fitness evolution over iterations
      
![Target String Problem](https://i.imgur.com/wI8rlnh.png)

      Figure 2: Graph of Target String evolution towards target 

![Deception](https://i.imgur.com/McwcOLO.png)

      Figure 3: Graph of Deception fitness evolution over iterations

## KnapSack Problem

For my representation of the Knapsack problem, I have 3 lists, 1 for the values of each item, another for the weights and the third which is then used for the fitness function is the ratio list of the value of an item over its weight. 

In order to represent the population, I initialise a random Boolean list of the same length as the number of items. This thus represents what items are in the user’s knapsack.

I implemented the Knapsack class across the same 8 functions:

•	initialisePopValues

•	calcFitness

•	selection

•	crossover

•	mutation

•	splitList

•	decision

•	method

For the Knapsack problem I implemented it in a very similar fashion with changes in the fitness function. This is done by shuffling the positions in which it checks the populations list values in order to make sure that the start and the end get equal treatment when sorting through the array and removing items that put the weight over max capacity. Another difference is the fact that if the fitness has been calculated as 0, then it will randomly append an item in order to ensure that the bag is not empty.

Results:

![Knapsack1](https://i.imgur.com/hfKaPtV.png)

![Knapsack2](https://i.imgur.com/kxp8LpK.png)

            Figure 4 & 5: Graph of Knapsack problem 1 & 2  fitness evolution over iterations
As this is less of a straightforward problem for the system in comparison to the OneMax problem we see a fluctuating erratic growth with an initial drop before a slow an unsteady increase. 
