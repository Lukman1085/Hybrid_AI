from calculate_fitness import calculate_fitness
from create_population import create_population
from selection import selection 
from crossover import crossover
from mutation import mutation
from regeneration import regeneration

target = "andi lukman"
besar_populasi = 10
populasi = create_population(target, besar_populasi)

print(populasi[0])

parent1, parent2 = selection(populasi) 

child1, child2 = crossover(parent1, parent2)

laju_mutasi = 0.3

mutant1 = mutation(child1, laju_mutasi)
mutant2 = mutation(child2, laju_mutasi)

mutant1['fitness'] = calculate_fitness(mutant1['gen'], target)
mutant2['fitness'] = calculate_fitness(mutant2['gen'], target)

children = [mutant1, mutant2]
new_populasi = regeneration(children, populasi)

print(new_populasi[0])