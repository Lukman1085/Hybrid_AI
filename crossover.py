def crossover(parent1, parent2):
    """Single-point crossover di titik tengah gen."""
    child1 = parent1.copy()
    child2 = parent2.copy()

    # Tentukan titik crossover (tengah)
    cp = round(len(parent1["gen"]) / 2)

    # Lakukan pertukaran gen di kiri titik crossover
    gen1 = list(child1["gen"])
    gen2 = list(child2["gen"])

    gen1[:cp], gen2[:cp] = gen2[:cp], gen1[:cp]

    # Update hasil crossover
    child1["gen"] = "".join(gen1)
    child2["gen"] = "".join(gen2)

    return child1, child2
