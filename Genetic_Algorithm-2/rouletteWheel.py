import numpy as np

def roulette_wheel(uk_pop, linear_fitness):
  """
  Memilih satu indeks orang tua menggunakan Roulette Wheel Selection.
  Versi ini menggunakan fungsi bawaan NumPy yang efisien.

  Argumen:
  uk_pop (int): Ukuran populasi.
  linear_fitness (np.ndarray): Vektor 1D berisi nilai fitness yang 
                                 sudah disesuaikan/diskalakan (LFR).

  Returns:
  int: Indeks (Pindex) dari kromosom yang terpilih (0-based).
  """
  
  # 1. Hitung total fitness
  jum_fitness = np.sum(linear_fitness)
  
  # 2. Safety check: Jika semua fitness 0, pilih acak
  if jum_fitness == 0:
    return np.random.randint(0, uk_pop)
    
  # 3. Normalisasi fitness menjadi probabilitas (total = 1.0)
  probabilitas = linear_fitness / jum_fitness
  
  # 4. Pilih satu indeks (dari 0 s/d uk_pop-1)
  #    berdasarkan array probabilitas
  #    MATLAB: a=uk_pop -> [0, 1, 2, ..., uk_pop-1]
  p_index = np.random.choice(a=uk_pop, p=probabilitas)
  
  return p_index

if __name__ == "__main__":
    # --- Contoh Penggunaan ---

    # Menggunakan LFR dari contoh 'LinearFitnessRanking' sebelumnya
    # Fitness Asli: [10.5, 80.2, 5.1, 45.0, 12.3]
    # LFR (skala baru): [0.95, 1.1, 0.9, 1.05, 1.0]
    lfr_contoh = np.array([0.95, 1.1, 0.9, 1.05, 1.0])
    uk_pop = 5

    print(f"Fitness LFR: {lfr_contoh}")
    print("Menjalankan Roulette Wheel 10 kali:")

    hasil_seleksi = []
    for _ in range(10):
        indeks_terpilih = roulette_wheel(uk_pop, lfr_contoh)
        hasil_seleksi.append(indeks_terpilih)

    print(hasil_seleksi)
    # Catatan: Hasilnya akan acak, tapi indeks 1 (fitness 1.1) 
    # dan indeks 3 (fitness 1.05) harusnya lebih sering muncul.