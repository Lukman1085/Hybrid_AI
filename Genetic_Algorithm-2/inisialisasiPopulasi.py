import numpy as np

def inisialisasi_populasi(uk_pop, jum_gen):
  """
  Membuat populasi awal secara acak.
  
  Argumen:
  uk_pop (int): Ukuran populasi (jumlah individu/kromosom).
  jum_gen (int): Jumlah gen dalam satu individu.
  
  Returns:
  numpy.ndarray: Matriks populasi (UkPop x JumGen) berisi 0 dan 1.
  """
  
  # Membuat matriks dengan ukuran (uk_pop, jum_gen)
  # dengan nilai integer acak antara 0 (inklusif) dan 2 (eksklusif),
  # yang berarti hanya menghasilkan 0 dan 1.
  populasi = np.random.randint(2, size=(uk_pop, jum_gen))
  
  return populasi


if __name__ == "__main__":
    # --- Contoh Penggunaan ---
    ukuran_populasi = 10  # Misal: 10 individu
    jumlah_gen = 8      # Misal: 8 gen per individu

    populasi_awal = inisialisasi_populasi(ukuran_populasi, jumlah_gen)

    print(f"Ukuran Populasi: {ukuran_populasi}")
    print(f"Jumlah Gen: {jumlah_gen}")
    print("--- Populasi Awal ---")
    print(populasi_awal)