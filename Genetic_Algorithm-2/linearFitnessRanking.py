import numpy as np

def linear_fitness_ranking(uk_pop, fitness, max_f, min_f):
  """
  Menskalakan nilai fitness ke ranking linear.
  Individu terburuk (fitness terendah) mendapat nilai min_f.
  Individu terbaik (fitness tertinggi) mendapat nilai max_f.

  Argumen:
  uk_pop (int): Ukuran populasi.
  fitness (np.ndarray): Vektor 1D (UkPop) berisi nilai fitness asli.
  max_f (float): Nilai fitness baru untuk individu TERBAIK (misal: 1.1).
  min_f (float): Nilai fitness baru untuk individu TERBURUK (misal: 0.9).

  Returns:
  np.ndarray: Vektor 1D (UkPop) berisi nilai fitness baru (LFR).
  """
  
  # 1. Dapatkan indeks yang akan MENGURUTKAN array fitness
  #    MATLAB: [SF, IndF] = sort(Fitness);
  #    ind_f[0] akan berisi indeks dari fitness TERKECIL (terburuk)
  #    ind_f[-1] akan berisi indeks dari fitness TERBESAR (terbaik)
  ind_f = np.argsort(fitness)
  
  # 2. Buat array nilai fitness baru yang terdistribusi linear
  #    dari min_f (untuk terburuk) ke max_f (untuk terbaik).
  scaled_values = np.linspace(min_f, max_f, uk_pop)
  
  # 3. Buat array hasil (LFR)
  lfr = np.zeros(uk_pop)
  
  # 4. Gunakan 'fancy indexing' untuk memetakan nilai baru ke
  #    posisi individu yang asli.
  #    Contoh: lfr[ind_f[0]] = scaled_values[0]
  #            (posisi individu terburuk = nilai terendah)
  lfr[ind_f] = scaled_values
  
  return lfr


if __name__ == "__main__":
    # --- Contoh Penggunaan ---

    # Misal UkPop = 5
    # Nilai fitness asli: [10.5, 80.2, 5.1, 45.0, 12.3]
    fitness_asli = np.array([10.5, 80.2, 5.1, 45.0, 12.3])
    uk_pop = 5

    # Kita tentukan ranking baru antara 0.9 (MinF) dan 1.1 (MaxF)
    min_f_baru = 0.9
    max_f_baru = 1.1

    lfr = linear_fitness_ranking(uk_pop, fitness_asli, max_f_baru, min_f_baru)

    print(f"Fitness Asli: {fitness_asli}")
    print(f"Fitness Baru (LFR): {lfr}")

    # --- Penjelasan Hasil Contoh ---
    # 1. ind_f = np.argsort(fitness_asli)
    #    -> [2, 0, 4, 3, 1]
    #    (indeks dari 5.1, 10.5, 12.3, 45.0, 80.2)
    #
    # 2. scaled_values = np.linspace(0.9, 1.1, 5)
    #    -> [0.9, 0.95, 1.0, 1.05, 1.1]
    #
    # 3. lfr[ind_f] = scaled_values
    #    -> lfr[[2, 0, 4, 3, 1]] = [0.9, 0.95, 1.0, 1.05, 1.1]
    #    Artinya:
    #    lfr[2] = 0.9   (fitness 5.1, terburuk)
    #    lfr[0] = 0.95  (fitness 10.5)
    #    lfr[4] = 1.0   (fitness 12.3)
    #    lfr[3] = 1.05  (fitness 45.0)
    #    lfr[1] = 1.1   (fitness 80.2, terbaik)
    #
    # 4. Hasil akhir 'lfr' (dalam urutan asli):
    #    [0.95, 1.1, 0.9, 1.05, 1.0]