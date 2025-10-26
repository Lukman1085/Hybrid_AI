def calculate_fitness(gen, target):
    """Menghitung persentase kesamaan karakter antara gen dan target."""
    matches = sum(1 for a, b in zip(gen, target) if a == b)
    fitness = (matches / len(target)) * 100
    return fitness
