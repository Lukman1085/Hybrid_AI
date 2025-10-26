from create_population import create_population
from selection import selection
from crossover import crossover

target = "Andi Lukman"
besar_populasi = 10
populasi = create_population(target, besar_populasi)

parent1, parent2 = selection(populasi)

child1, child2 = crossover(parent1, parent2)

print(f"Parent 1: {parent1['gen']} with fitness {parent1['fitness']}")
print(f"Parent 2: {parent2['gen']} with fitness {parent2['fitness']}")
print(f"Child 1: {child1['gen']} with fitness {child1['fitness']}")
print(f"Child 2: {child2['gen']} with fitness {child2['fitness']}")