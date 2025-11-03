import numpy as np

def dekodekan_kromosom(kromosom, n_var, n_bit, ra, rb):
  """
  Mendekodekan kromosom biner menjadi individu bernilai real.

  Argumen:
  kromosom (np.ndarray): Matriks 1D (JumGen) berisi gen biner (0 atau 1).
  n_var (int): Jumlah variabel yang dikodekan dalam kromosom.
  n_bit (int): Jumlah bit yang digunakan untuk mengkodekan SATU variabel.
  ra (float): Batas atas interval (contoh: 5.0).
  rb (float): Batas bawah interval (contoh: -5.0).

  Returns:
  np.ndarray: Vektor 1D (Nvar) berisi nilai real hasil dekode.
  """
  
  # 1. Pastikan ukuran kromosom sesuai
  jum_gen = len(kromosom)
  if jum_gen != n_var * n_bit:
    raise ValueError(
        f"Ukuran Kromosom ({jum_gen}) tidak cocok dengan "
        f"Nvar * Nbit ({n_var * n_bit})"
    )

  # 2. Buat vektor pangkat [2^-1, 2^-2, ..., 2^-Nbit]
  #    MATLAB: 2.^(-(1:Nbit))
  pangkat = 2.0 ** (-np.arange(1, n_bit + 1))
  
  # 3. Reshape kromosom dari [1, 0, 1, 1, 0, 1] -> [[1, 0, 1], [1, 0, 1]]
  #    (jika Nvar=2, Nbit=3)
  matriks_bit = kromosom.reshape((n_var, n_bit))
  
  # 4. Hitung nilai desimal [0, 1] untuk setiap variabel
  #    Ini adalah inti pengganti loop 'for' di MATLAB
  #    Menggunakan perkalian matriks (dot product)
  x_normalized = matriks_bit @ pangkat
  
  # 5. Skalakan nilai dari [0, 1] ke rentang [Rb, Ra]
  #    MATLAB: x(ii) = Rb + (Ra-Rb)*x(ii)
  x_decoded = rb + (ra - rb) * x_normalized
  
  return x_decoded


if __name__ == "__main__":
    # --- Contoh Penggunaan ---

    # Misal kita punya 1 kromosom
    # Gen = [1, 0, 1, 1, 0, 0, 1, 0]
    # Kita ingin dekode jadi 2 variabel (Nvar = 2)
    # Masing-masing variabel pakai 4 bit (Nbit = 4)
    # Rentang nilainya antara -5 (Rb) dan 5 (Ra)

    kromosom_contoh = np.array([1, 0, 1, 1, 0, 0, 1, 0])
    n_var = 2
    n_bit = 4
    ra = 5.0  # Batas atas
    rb = -5.0 # Batas bawah

    individu_x = dekodekan_kromosom(kromosom_contoh, n_var, n_bit, ra, rb)

    print(f"Kromosom (Biner): {kromosom_contoh}")
    print(f"Hasil Dekode (Real): {individu_x}")

    # Penjelasan hasil contoh:
    # Var 1: [1, 0, 1, 1] -> (1*2^-1 + 0*2^-2 + 1*2^-3 + 1*2^-4) = (0.5 + 0 + 0.125 + 0.0625) = 0.6875
    #   Skala: -5 + (5 - (-5)) * 0.6875 = -5 + 10 * 0.6875 = -5 + 6.875 = 1.875
    # Var 2: [0, 0, 1, 0] -> (0*2^-1 + 0*2^-2 + 1*2^-3 + 0*2^-4) = (0 + 0 + 0.125 + 0) = 0.125
    #   Skala: -5 + (5 - (-5)) * 0.125 = -5 + 10 * 0.125 = -5 + 1.25 = -3.75
    # Hasil: [1.875, -3.75]