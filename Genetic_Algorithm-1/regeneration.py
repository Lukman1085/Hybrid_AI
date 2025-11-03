def regeneration(children, populasi):
    """Ganti individu dengan fitness terendah menggunakan anak-anak baru."""
    new_populasi = populasi.copy()
    # Ambil semua nilai fitness dari populasi lama
    fitness = [ind["fitness"] for ind in new_populasi]

    # Hapus individu dengan fitness terendah sebanyak jumlah anak
    for _ in range(len(children)):
        if not fitness:
            break   

        # Cari indeks dengan fitness minimum
        min_index = fitness.index(min(fitness))
        # Hapus individu tersebut
        new_populasi.pop(min_index)
        fitness.pop(min_index)

    # Tambahkan anak-anak baru ke populasi
    for child in children:
        new_populasi.append(child)

    # Kembalikan populasi baru
    return new_populasi


