import numpy as np

def pindah_silang(bapak, ibu):
  """
  Melakukan single-point crossover (pindah silang satu titik) 
  antara dua orang tua untuk menghasilkan dua anak.

  Argumen:
  bapak (np.ndarray): Kromosom 1D orang tua 1 (Bapak).
  ibu (np.ndarray): Kromosom 1D orang tua 2 (Ibu).

  Returns:
  tuple (np.ndarray, np.ndarray): Sepasang kromosom anak (anak1, anak2).
  """
  
  # 1. Dapatkan jumlah gen dari salah satu orang tua
  #    (Asumsi bapak dan ibu punya panjang yang sama)
  jum_gen = len(bapak)
  
  # Jika kromosom terlalu pendek, tidak bisa dipotong
  if jum_gen <= 1:
    return bapak.copy(), ibu.copy()
    
  # 2. Tentukan Titik Potong (TP)
  # MATLAB: TP = 1 + fix(rand*(JumGen-1));
  # Ini menghasilkan integer acak dalam rentang [1, JumGen-1]
  
  # Python (NumPy): np.random.randint(low, high)
  # 'low' inklusif, 'high' EKSKLUSIF.
  # Untuk mendapatkan rentang [1, JumGen-1] (inklusif),
  # kita harus set 'high' = JumGen.
  tp = np.random.randint(1, jum_gen)
  
  # 3. Buat Anak 1
  # MATLAB: Anak(1,:) = [Bapak(1:TP) Ibu(TP+1:JumGen)];
  # Python:
  # Bapak(1:TP)     -> bapak[:tp]  (indeks 0 s/d tp-1)
  # Ibu(TP+1:JumGen) -> ibu[tp:]   (indeks tp s/d akhir)
  anak1 = np.concatenate([bapak[:tp], ibu[tp:]])
  
  # 4. Buat Anak 2
  # MATLAB: Anak(2,:) = [Ibu(1:TP) Bapak(TP+1:JumGen)];
  # Python:
  # Ibu(1:TP)       -> ibu[:tp]
  # Bapak(TP+1:JumGen) -> bapak[tp:]
  anak2 = np.concatenate([ibu[:tp], bapak[tp:]])
  
  return anak1, anak2

if __name__ == "__main__":
    # --- Contoh Penggunaan ---

    # Misal JumGen = 10
    bapak_contoh = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ibu_contoh   = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

    # Panggil fungsi
    # Kita tidak perlu 'jum_gen' sebagai argumen, 
    # karena Python bisa ambil dari 'len(bapak)'
    anak_a, anak_b = pindah_silang(bapak_contoh, ibu_contoh)

    print(f"Bapak: {bapak_contoh}")
    print(f"Ibu  : {ibu_contoh}")
    print("--- Setelah Pindah Silang (Titik Potong Acak) ---")
    print(f"Anak 1: {anak_a}")
    print(f"Anak 2: {anak_b}")

    # Contoh jika TP (titik potong) = 4:
    # Anak 1: [0, 0, 0, 0] + [1, 1, 1, 1, 1, 1] -> [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    # Anak 2: [1, 1, 1, 1] + [0, 0, 0, 0, 0, 0] -> [1, 1, 1, 1, 0, 0, 0, 0, 0, 0]