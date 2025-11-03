import numpy as np
import matplotlib.pyplot as plt
from inisialisasiPopulasi import inisialisasi_populasi
from dekodekanKromosom import dekodekan_kromosom
from evaluasiIndividu import evaluasi_individu
from linearFitnessRanking import linear_fitness_ranking 
from rouletteWheel import roulette_wheel
from pindahSilang import pindah_silang
from mutasi import mutasi

if __name__ == "__main__":
    print("Memulai Algoritma Genetika Standar...")

    n_var = 2        # Jumlah variabel pada fungsi yang dioptimasi
    n_bit = 10       # Jumlah bit yang mengkodekan satu variabel
    jum_gen = n_bit * n_var # Jumlah gen dalam kromosom
    rb = -5.12     # Batas bawah interval
    ra = 5.12      # Batas atas interval

    uk_pop = 200     # Jumlah kromosom dalam populasi
    p_silang = 0.8   # Probabilitas pindah silang
    p_mutasi = 0.05  # Probabilitas mutasi
    max_g = 100      # Jumlah generasi

    bil_kecil = 10**-1       # Digunakan untuk menghindari pembagian dengan 0
    f_threshold = 1 / bil_kecil # Threshold untuk nilai Fitness
    bgraf = f_threshold      # Untuk menangani tampilan grafis

    # Aktifkan mode interaktif
    plt.ion()

    fig, ax = plt.subplots(figsize=(8, 6)) # setara 'figure'
    ax.set_title('Optimasi fungsi menggunakan AG standar (Python)')
    ax.set_xlim(1, max_g)
    ax.set_ylim(0, bgraf)
    ax.set_xlabel('Generasi')
    ax.set_ylabel('Fitness terbaik')

    # Siapkan data plot
    generasi_plot = np.arange(1, max_g + 1)
    plot_vector = np.zeros(max_g)

    # Buat objek plot (garis)
    # Perhatikan koma di 'hbestplot,'
    hbestplot, = ax.plot(generasi_plot, plot_vector, 'b-') # 'b-' = blue line

    # Buat objek teks
    htext1 = ax.text(0.6 * max_g, 0.25 * bgraf, f'Fitness terbaik: {0.0:7.4f}')
    htext2 = ax.text(0.6 * max_g, 0.20 * bgraf, f'Variabel X1: {0.0:5.4f}')
    htext3 = ax.text(0.6 * max_g, 0.15 * bgraf, f'Variabel X2: {0.0:5.4f}')
    htext4 = ax.text(0.6 * max_g, 0.10 * bgraf, f'Nilai minimum: {0.0:5.4f}')

    # Tampilkan plot awal
    fig.canvas.draw()
    plt.pause(0.1) # setara 'drawnow'

    populasi = inisialisasi_populasi(uk_pop, jum_gen)

    # Variabel untuk menyimpan data terbaik
    best_x = np.zeros(n_var)
    max_f = 0.0

    # MATLAB: for generasi=1:MaxG
    for generasi in range(max_g):
        
        # --- Evaluasi Populasi ---
        fitness = np.zeros(uk_pop)
        
        # Evaluasi individu pertama (indeks 0)
        x = dekodekan_kromosom(populasi[0], n_var, n_bit, ra, rb)
        fitness[0] = evaluasi_individu(x, bil_kecil)
        max_f = fitness[0]
        min_f = fitness[0]
        indeks_individu_terbaik = 0
        best_x = x # Inisialisasi BestX
        
        # Evaluasi sisa populasi
        # MATLAB: for ii=2:UkPop
        for ii in range(1, uk_pop):
            kromosom = populasi[ii]
            x = dekodekan_kromosom(kromosom, n_var, n_bit, ra, rb)
            fitness[ii] = evaluasi_individu(x, bil_kecil)
            
            if fitness[ii] > max_f:
                max_f = fitness[ii]
                indeks_individu_terbaik = ii # Indeks 0-based
                best_x = x
                
            if fitness[ii] < min_f:
                min_f = fitness[ii]
                
        # --- Penanganan Grafis 2D ---
        plot_vector[generasi] = max_f
        hbestplot.set_ydata(plot_vector)
        
        htext1.set_text(f'Fitness terbaik: {max_f:7.4f}')
        htext2.set_text(f'Variabel X1: {best_x[0]:5.4f}')
        htext3.set_text(f'Variabel X2: {best_x[1]:5.4f}')
        
        nilai_min_cost = (1.0 / max_f) - bil_kecil
        htext4.set_text(f'Nilai minimum: {nilai_min_cost:5.4f}')
        
        # Update plot
        fig.canvas.draw()
        plt.pause(0.01) # setara 'drawnow'
        
        print(f"Gen: {generasi+1} | Fitness Terbaik: {max_f:7.4f} | Cost Min: {nilai_min_cost:5.4f} | X: [{best_x[0]:.4f}, {best_x[1]:.4f}]")

        # --- Cek Kondisi Berhenti ---
        if max_f >= f_threshold:
            print("Threshold fitness tercapai. Berhenti.")
            break
            
        # --- Elitisme ---
        # Salin populasi (PENTING: .copy())
        temp_populasi = populasi.copy()
        
        # MATLAB: if mod(UkPop,2)==0
        if uk_pop % 2 == 0:
            # Populasi GENAP: Salin 2 individu terbaik
            # MATLAB: IterasiMulai = 3; (indeks 1-based)
            iterasi_mulai = 2 # Python: mulai dari indeks 2 (0-based)
            temp_populasi[0] = populasi[indeks_individu_terbaik]
            temp_populasi[1] = populasi[indeks_individu_terbaik]
        else:
            # Populasi GANJIL: Salin 1 individu terbaik
            # MATLAB: IterasiMulai = 2;
            iterasi_mulai = 1 # Python: mulai dari indeks 1
            temp_populasi[0] = populasi[indeks_individu_terbaik]

        # --- Ranking ---
        linear_fitness = linear_fitness_ranking(uk_pop, fitness, max_f, min_f)

        # --- Roulette-wheel dan Pindah Silang ---
        # MATLAB: for jj=IterasiMulai:2:UkPop
        for jj in range(iterasi_mulai, uk_pop, 2):
            # Pilih 2 orang tua
            ip1 = roulette_wheel(uk_pop, linear_fitness)
            ip2 = roulette_wheel(uk_pop, linear_fitness)
            
            # Cek probabilitas pindah silang
            # MATLAB: if (rand < Psilang)
            if np.random.rand() < p_silang:
                # Lakukan pindah silang
                anak1, anak2 = pindah_silang(populasi[ip1], populasi[ip2])
                temp_populasi[jj] = anak1
                temp_populasi[jj+1] = anak2
            else:
                # Tidak pindah silang (langsung salin)
                temp_populasi[jj] = populasi[ip1]
                temp_populasi[jj+1] = populasi[ip2]
                
        # --- Mutasi ---
        # Mutasi dilakukan pada semua kromosom BARU
        # MATLAB: for kk=IterasiMulai:UkPop
        for kk in range(iterasi_mulai, uk_pop):
            temp_populasi[kk] = mutasi(temp_populasi[kk], p_mutasi)
            
        # --- Generational Replacement ---
        # Populasi baru menggantikan populasi lama
        populasi = temp_populasi
        
    print("\nEvolusi Selesai.")
    print("--- Hasil Akhir ---")
    print(f"Generasi Terakhir: {generasi+1}")
    print(f"Fitness Terbaik: {max_f:7.4f}")
    print(f"Nilai Minimum Cost: {nilai_min_cost:5.4f}")
    print(f"Variabel (X1, X2): [{best_x[0]:.4f}, {best_x[1]:.4f}]")


    # Matikan mode interaktif dan tahan plot terakhir
    plt.ioff()
    plt.title("HASIL AKHIR - Optimasi fungsi menggunakan AG standar")
    plt.show()