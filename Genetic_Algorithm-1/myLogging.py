def logging(populasi, target, solusi, generasi):
    """Mencatat informasi populasi pada setiap generasi."""
    print(f"Target: {target}")
    print(f'solusi: {solusi["gen"]}')
    print(f"Generasi {generasi}:")
    for individu in populasi:
        print(f"Gen: {individu['gen']}, Fitness: {individu['fitness']}")
    