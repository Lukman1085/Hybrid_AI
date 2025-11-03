import random
from calculate_fitness import calculate_fitness
from create_gen import create_gen


target = "Andi Lukman"
panjang_target = len(target)
gen_baru = create_gen(panjang_target)

fitness = calculate_fitness(gen_baru, target)

print(f"target: {target}")
print(f"gen_baru: {gen_baru}")
print(f"fitness: {fitness}")