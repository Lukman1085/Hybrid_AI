import numpy as np
import matplotlib.pyplot as plt
from inisialisasiPopulasi import inisialisasi_populasi
from dekodekanKromosom import dekodekan_kromosom
from evaluasiIndividu import evaluasi_individu
from linearFitnessRanking import linear_fitness_ranking 
from rouletteWheel import roulette_wheel
from pindahSilang import pindah_silang
from mutasi import mutasi

print("Memulai Uji Coba Batch Algoritma Genetika...")

n_var = 2        # Jumlah variabel
n_bit = 10       # Jumlah bit per variabel
jum_gen = n_bit * n_var
rb = -5.12       # Batas bawah
ra = 5.12        # Batas atas

uk_pop = 200     # Ukuran populasi
p_silang = 0.8   # Probabilitas pindah silang
p_mutasi = 0.05  # Probabilitas mutasi
max_g = 100      # Jumlah generasi MAKSIMUM per uji coba

bil_kecil = 10**-1
f_threshold = 1 / bil_kecil # Target fitness (cost = 0)

# --- Parameter Uji Coba Batch ---
JUMLAH_UJI_COBA = 50  # Ubah ini (misal: 100, 500)
NAMA_FILE_OUTPUT = "hasil_ag_batch.csv"

hasil_uji_coba = []

for uji in range(JUMLAH_UJI_COBA):
    
    print(f"--- Memulai Uji Coba ke-{uji + 1} / {JUMLAH_UJI_COBA} ---")
    
    populasi = inisialisasi_populasi(uk_pop, jum_gen)
    generasi_tercapai = np.nan 
    
    for generasi in range(max_g):
        
        # --- Evaluasi Populasi ---
        fitness = np.zeros(uk_pop)
        
        x = dekodekan_kromosom(populasi[0], n_var, n_bit, ra, rb)
        fitness[0] = evaluasi_individu(x, bil_kecil)
        max_f = fitness[0]
        min_f = fitness[0]
        indeks_individu_terbaik = 0
        best_x = x
        
        for ii in range(1, uk_pop):
            kromosom = populasi[ii]
            x = dekodekan_kromosom(kromosom, n_var, n_bit, ra, rb)
            fitness[ii] = evaluasi_individu(x, bil_kecil)
            
            if fitness[ii] > max_f:
                max_f = fitness[ii]
                indeks_individu_terbaik = ii
                best_x = x
            if fitness[ii] < min_f:
                min_f = fitness[ii]

        if (generasi + 1) % 50 == 0 or generasi == 0:
            nilai_min_cost = (1.0 / max_f) - bil_kecil
            print(f"  Uji {uji+1}, Gen: {generasi+1} | Cost Min: {nilai_min_cost:5.4f}")

        # --- Cek Kondisi Berhenti (Solusi Ditemukan) ---
        if max_f >= f_threshold:
            print(f"  *** Solusi ditemukan pada Generasi {generasi + 1}! ***")
            generasi_tercapai = generasi + 1 
            break 
            
        # --- Elitisme ---
        temp_populasi = populasi.copy()
        
        if uk_pop % 2 == 0:
            iterasi_mulai = 2 
            temp_populasi[0] = populasi[indeks_individu_terbaik]
            temp_populasi[1] = populasi[indeks_individu_terbaik]
        else:
            iterasi_mulai = 1
            temp_populasi[0] = populasi[indeks_individu_terbaik]

        # --- Ranking ---
        linear_fitness = linear_fitness_ranking(uk_pop, fitness, max_f, min_f)

        # --- Roulette-wheel dan Pindah Silang ---
        for jj in range(iterasi_mulai, uk_pop, 2):
            ip1 = roulette_wheel(uk_pop, linear_fitness)
            ip2 = roulette_wheel(uk_pop, linear_fitness)
            
            if np.random.rand() < p_silang:
                anak1, anak2 = pindah_silang(populasi[ip1], populasi[ip2])
                temp_populasi[jj] = anak1
                temp_populasi[jj+1] = anak2
            else:
                temp_populasi[jj] = populasi[ip1]
                temp_populasi[jj+1] = populasi[ip2]
                
        # --- Mutasi ---
        for kk in range(iterasi_mulai, uk_pop):
            temp_populasi[kk] = mutasi(temp_populasi[kk], p_mutasi)
            
        # --- Generational Replacement ---
        populasi = temp_populasi
    
    hasil_uji_coba.append([uji + 1, generasi_tercapai])

print(f"\n...Semua {JUMLAH_UJI_COBA} uji coba selesai.")

hasil_array = np.array(hasil_uji_coba)

try:
    np.savetxt(
        NAMA_FILE_OUTPUT,
        hasil_array,
        delimiter=',',
        header='Uji_Ke,Generasi_Terbaik',
        comments='',
        fmt=['%d', '%.1f']
    )
    print(f"Hasil telah disimpan ke file: {NAMA_FILE_OUTPUT}")
except Exception as e:
    print(f"Gagal menyimpan file data: {e}")

# Ambil hanya kolom hasil (kolom ke-1, indeks 1)
hasil_generasi = hasil_array[:, 1]

# Hitung jumlah sukses (bukan 'nan') dan gagal ('nan')
jumlah_sukses = np.count_nonzero(~np.isnan(hasil_generasi))
jumlah_gagal = JUMLAH_UJI_COBA - jumlah_sukses
tingkat_sukses = (jumlah_sukses / JUMLAH_UJI_COBA) * 100

print("\n--- Rangkuman Statistik Uji Coba ---")
print(f"Total Uji Coba   : {JUMLAH_UJI_COBA}")
print(f"Total Sukses     : {jumlah_sukses} ({tingkat_sukses:.2f}%)")
print(f"Total Gagal      : {jumlah_gagal}")

# Hanya hitung statistik jika ada setidaknya satu yang sukses
if jumlah_sukses > 0:
    # np.nanmean, .nanmin, .nanmax, .nanstd
    # akan menghitung statistik dengan MENGABAIKAN nilai 'nan' (gagal)
    
    rata_rata = np.nanmean(hasil_generasi)
    minimum = np.nanmin(hasil_generasi)
    maksimum = np.nanmax(hasil_generasi)
    std_deviasi = np.nanstd(hasil_generasi)

    print("\n--- Statistik Generasi (Hanya Uji Sukses) ---")
    print(f"Rata-rata Gen.   : {rata_rata:.2f}")
    print(f"Generasi Min     : {minimum:.0f} (Tercepat)")
    print(f"Generasi Max     : {maksimum:.0f} (Terlambat)")
    print(f"Std. Deviasi     : {std_deviasi:.2f}")
    
    # Siapkan teks untuk disimpan ke file
    summary_text = (
        f"\n\n--- Rangkuman Statistik ---,"
        f"\nTotal Uji Coba,{JUMLAH_UJI_COBA},"
        f"\nTotal Sukses,{jumlah_sukses},"
        f"\nTotal Gagal,{jumlah_gagal},"
        f"\nTingkat Sukses (%),{tingkat_sukses:.2f},"
        f"\n--- Statistik Generasi (Hanya Uji Sukses) ---,"
        f"\nRata-rata,{rata_rata:.2f},"
        f"\nMinimum (Tercepat),{minimum:.0f},"
        f"\nMaksimum (Terlambat),{maksimum:.0f},"
        f"\nStd. Deviasi,{std_deviasi:.2f},"
    )
else:
    print("\n--- Statistik Generasi (Tidak ada uji sukses) ---")
    summary_text = (
        f"\n\n--- Rangkuman Statistik ---,"
        f"\nTotal Uji Coba,{JUMLAH_UJI_COBA},"
        f"\nTotal Sukses,0,"
        f"\nTotal Gagal,{JUMLAH_UJI_COBA},"
        f"\nTingkat Sukses (%),0.00,"
    )

# Coba tambahkan (append) rangkuman ke file CSV
try:
    with open(NAMA_FILE_OUTPUT, 'a') as f:
        f.write(summary_text)
    print(f"Rangkuman statistik juga ditambahkan ke {NAMA_FILE_OUTPUT}")
except Exception as e:
    print(f"Gagal menambahkan rangkuman ke file: {e}")

# --- Program Selesai ---