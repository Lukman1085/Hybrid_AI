from calculate_fitness import calculate_fitness
from create_population import create_population
from selection import selection 
from crossover import crossover
from mutation import mutation

target = "Andi Lukman"
besar_populasi = 10
populasi = create_population(target, besar_populasi)

parent1, parent2 = selection(populasi) 

child1, child2 = crossover(parent1, parent2)

laju_mutasi = 0.3

mutant1 = mutation(child1, laju_mutasi)
mutant2 = mutation(child2, laju_mutasi)

mutant1['fitness'] = calculate_fitness(mutant1['gen'], target)
mutant2['fitness'] = calculate_fitness(mutant2['gen'], target)

print(f"Child 1: {child1['gen']} with fitness {child1['fitness']}")
print(f"Mutant 1: {mutant1['gen']} with fitness {mutant1['fitness']}")