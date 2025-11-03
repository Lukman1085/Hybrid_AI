from calculate_fitness import calculate_fitness
from create_population import create_population
from selection import selection 
from crossover import crossover
from mutation import mutation
from regeneration import regeneration
from termination import termination
from myLogging import logging

def simpleGA(target, besar_populasi, laju_mutasi):
    populasi = create_population(target, besar_populasi)
    isLooping = True
    generasi = 0

    while isLooping:

        parent1, parent2 = selection(populasi) 

        child1, child2 = crossover(parent1, parent2)

        laju_mutasi = 0.3

        mutant1 = mutation(child1, laju_mutasi)
        mutant2 = mutation(child2, laju_mutasi)

        mutant1['fitness'] = calculate_fitness(mutant1['gen'], target)
        mutant2['fitness'] = calculate_fitness(mutant2['gen'], target)

        children = [mutant1, mutant2]
        populasi = regeneration(children, populasi)
        generasi += 1

        isLooping, solusi = termination(populasi)
        #logging(populasi, target, solusi, generasi)

    return solusi, generasi