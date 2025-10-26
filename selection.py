# def selection(populasi):
#     """Memilih dua individu terbaik berdasarkan fitness tertinggi."""
#     # Ambil semua nilai fitness
#     fitness_data = [individu["fitness"] for individu in populasi]

#     # Parent 1 (fitness tertinggi)
#     index1 = fitness_data.index(max(fitness_data))
#     parent1 = populasi[index1]

#     # Hapus parent1 agar tidak terpilih dua kali
#     populasi.pop(index1)
#     fitness_data.pop(index1)

#     # Parent 2 (fitness tertinggi berikutnya)
#     index2 = fitness_data.index(max(fitness_data))
#     parent2 = populasi[index2]

#     return parent1, parent2

def selection(populasi):
    # Pastikan populasi tidak kosong
    if not populasi:
        raise ValueError("Populasi kosong, tidak bisa melakukan seleksi.")

    # Ambil semua nilai fitness
    fitness_data = [individu["fitness"] for individu in populasi]

    # Ambil individu dengan fitness tertinggi (parent1)
    index1 = fitness_data.index(max(fitness_data))
    parent1 = populasi[index1]

    # Hapus parent1 dari daftar sementara
    populasi_temp = populasi[:index1] + populasi[index1 + 1:]
    fitness_temp = fitness_data[:index1] + fitness_data[index1 + 1:]

    # Ambil individu terbaik kedua (parent2)
    index2 = fitness_temp.index(max(fitness_temp))
    parent2 = populasi_temp[index2]

    return parent1, parent2



