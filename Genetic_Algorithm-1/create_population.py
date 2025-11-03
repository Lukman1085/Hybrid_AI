from create_gen import create_gen
from calculate_fitness import calculate_fitness

def create_population(target, besar_populasi):
    """Membuat populasi awal dengan gen acak dan fitness masing-masing."""
    populasi = []
    for _ in range(besar_populasi):
        gen = create_gen(len(target))
        fitness = calculate_fitness(gen, target)
        individu = {
            "gen": gen,
            "fitness": fitness
        }
        populasi.append(individu)
    return populasi
