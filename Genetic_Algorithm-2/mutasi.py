import numpy as np

def mutasi(kromosom, p_mutasi):
  """
  Melakukan mutasi bit-flip pada sebuah kromosom.
  Versi ini menggunakan vektorisasi NumPy (tanpa loop 'for').

  Argumen:
  kromosom (np.ndarray): Kromosom 1D (individu) yang akan dimutasi.
  p_mutasi (float): Probabilitas mutasi (misal: 0.01).

  Returns:
  np.ndarray: Kromosom baru hasil mutasi.
  """
  
  # 1. Buat salinan kromosom agar tidak mengubah yang asli
  #    INI SANGAT PENTING!
  mut_krom = kromosom.copy()
  
  # Dapatkan jumlah gen
  jum_gen = len(mut_krom)
  
  # 2. Buat array berisi angka acak [0, 1] 
  #    sejumlah 'jum_gen'
  random_rolls = np.random.rand(jum_gen)
  
  # 3. Buat 'mask' boolean. 
  #    'True' jika gen harus mutasi, 'False' jika tidak.
  #    MATLAB: if (rand < Pmutasi)
  mask_mutasi = random_rolls < p_mutasi
  
  # 4. Terapkan bit-flip (1 - x) HANYA pada gen 
  #    yang terkena mutasi (dimana mask == True)
  #    
  #    Logika '1 - x':
  #    Jika mut_krom[i] = 0 -> 1 - 0 = 1
  #    Jika mut_krom[i] = 1 -> 1 - 1 = 0
  mut_krom[mask_mutasi] = 1 - mut_krom[mask_mutasi]
  
  return mut_krom


if __name__ == "__main__":
    # --- Contoh Penggunaan ---
    # Misal probabilitas mutasi = 10% (0.1)
    prob_mutasi = 0.1
    kromosom_asli = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    print(f"Kromosom Asli : {kromosom_asli}")

    # Jalankan beberapa kali untuk melihat hasil acak
    for i in range(3):
        kromosom_baru = mutasi(kromosom_asli, prob_mutasi)
        print(f"Hasil Mutasi {i+1} : {kromosom_baru}")