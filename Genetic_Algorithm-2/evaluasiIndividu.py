import numpy as np

def evaluasi_individu(x, bil_kecil):
  """
  Mengevaluasi individu (x) untuk mendapatkan nilai fitness-nya.
  
  Ini adalah 'objective function' spesifik yang ingin dioptimalkan.
  Fungsi cost (yang akan diminimalkan):
  f(x1, x2) = 1000*(x1 - 2*x2)^2 + (1-x1)^2
  
  Fitness (yang akan dimaksimalkan) dihitung sebagai:
  Fitness = 1 / (f(x1, x2) + bil_kecil)
  
  Argumen:
  x (np.ndarray): Individu (vektor 1D) berisi nilai real [x1, x2].
  bil_kecil (float): Angka kecil untuk menghindari pembagian nol.
  
  Returns:
  float: Nilai fitness dari individu.
  """
  
  # Pastikan 'x' adalah array numpy untuk konsistensi
  # (Meskipun list biasa juga bisa bekerja untuk indexing [0] dan [1])
  x = np.asarray(x)
  
  # Ambil variabel x1 dan x2 dari individu
  # MATLAB: x(1) -> Python: x[0] (karena Python 0-indexed)
  # MATLAB: x(2) -> Python: x[1]
  x1 = x[0]
  x2 = x[1]
  
  # Hitung dua bagian dari 'cost function'
  # MATLAB: ^2 -> Python: **2
  term1 = 1000.0 * (x1 - 2.0 * x2)**2
  term2 = (1.0 - x1)**2
  
  # Jumlahkan cost-nya
  cost = term1 + term2
  
  # Hitung fitness (kebalikan dari cost)
  fitness = 1.0 / (cost + bil_kecil)
  
  return fitness


if __name__ == "__main__":
    # --- Contoh Penggunaan ---

    # Nilai kecil untuk menghindari pembagian dengan nol
    bil_kecil = 1e-10  # 0.0000000001

    # 1. Uji solusi yang (seharusnya) optimal
    # Cost = 0 jika (1-x1) = 0 -> x1 = 1
    # dan (x1 - 2*x2) = 0 -> (1 - 2*x2) = 0 -> x2 = 0.5
    individu_optimal = np.array([1.0, 0.5])
    fitness_opt = evaluasi_individu(individu_optimal, bil_kecil)

    print(f"Individu Optimal: {individu_optimal}")
    # Hasilnya akan sangat besar (1 / 1e-10)
    print(f"Fitness Optimal: {fitness_opt:e}") 


    # 2. Uji solusi lain (misal: [0, 0])
    # Cost = 1000*(0-0)^2 + (1-0)^2 = 1
    # Fitness = 1 / (1 + bil_kecil) ≈ 1.0
    individu_lain = np.array([0.0, 0.0])
    fitness_lain = evaluasi_individu(individu_lain, bil_kecil)

    print(f"\nIndividu Lain: {individu_lain}")
    print(f"Fitness Lain: {fitness_lain}")