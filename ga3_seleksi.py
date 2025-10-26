from create_population import create_population
from selection import selection

target = "Andi Lukman"
besar_populasi = 10
populasi = create_population(target, besar_populasi)

parent1, parent2 = selection(populasi)

print(f"Parent 1: {parent1['gen']} with fitness {parent1['fitness']}")
print(f"Parent 2: {parent2['gen']} with fitness {parent2['fitness']}")