import numpy as np
import matplotlib.pyplot as plt
import json
import random

from BangMatrixIT import BangMatrixIT
from InisialisasiPopulasi import inisialisasi_populasi
from DekodekanKromosom import dekodekan_kromosom
from BinaryEvalInd import BinaryEvalInd
from LinearFitnessRanking import linear_fitness_ranking
from RouletteWheel import roulette_wheel
from PindahSilang import pindah_silang
from Mutasi import mutasi


# ==============================
# PARAMETER GA
# ==============================
JumMasukan = 3
JPmasukan = 2**JumMasukan
Nbit = 20
JumGen = Nbit * (JumMasukan + 1)**2
Nvar = int(JumGen / Nbit)

Rb = -10
Ra = 10
MinDelta = 0.01
Fthreshold = 1 / MinDelta
Bgraf = Fthreshold

UkPop = 100
Psilang = 0.8
Pmutasi = 0.03
MaxG = 2000


# ==============================
# GRAFIK
# ==============================
plt.ion()
fig, ax = plt.subplots(figsize=(6, 4))
fig.canvas.manager.set_window_title("Algoritma Genetika")

ax.set_title("Algoritma Genetika untuk Pelatihan FFNN (Binary Encoding)")
ax.set_xlim(1, MaxG)
ax.set_ylim(0, Bgraf)

best_arr = np.zeros(MaxG)
avg_arr = np.zeros(MaxG)

hbest, = ax.plot(range(1, MaxG+1), best_arr, label="Fitness Terbaik")
havg, = ax.plot(range(1, MaxG+1), avg_arr, label="Fitness Rata-rata")

ax.set_xlabel("Generasi")
ax.set_ylabel("Fitness")
ax.legend()
plt.draw()
plt.pause(0.01)


# ==============================
# DATASET (IM & TM)
# ==============================
IM, TM = BangMatrixIT(JumMasukan, JPmasukan)


# ==============================
# POPULASI AWAL
# ==============================
Populasi = inisialisasi_populasi(UkPop, JumGen)


# ==============================
# VARIABEL BEST SEPANJANG SEJARAH
# ==============================
best_global_fitness = -999999999
best_global_chrom = None


# ==============================
# LOOP GA
# ==============================
for generasi in range(1, MaxG + 1):

    fitness = np.zeros(UkPop)

    # ========== HITUNG FITNESS ==========
    for i in range(UkPop):
        FFNNstruk = dekodekan_kromosom(Populasi[i], Nvar, Nbit, Ra, Rb)
        fitness[i] = BinaryEvalInd(FFNNstruk, JumMasukan, JPmasukan, IM, TM)

    # Info generasi
    MaxF = np.max(fitness)
    MinF = np.min(fitness)
    idx_best = np.argmax(fitness)

    print(f"Generasi {generasi}: MaxF={MaxF:.5f}, MinF={MinF:.5f}")

    # Simpan best global sepanjang sejarah
    if MaxF > best_global_fitness:
        best_global_fitness = MaxF
        best_global_chrom = Populasi[idx_best].copy()

    # ========== UPDATE GRAFIK ==========
    best_arr[generasi-1] = MaxF
    avg_arr[generasi-1] = np.mean(fitness)

    hbest.set_ydata(best_arr)
    havg.set_ydata(avg_arr)
    plt.pause(0.01)

    # ========== STOP JIKA FIT THRESHOLD TERCAPAI ==========
    if MaxF >= Fthreshold:
        print(">>> Threshold tercapai. GA berhenti.")
        break

    # =======================
    # SELEKSI (RANKING + ROULETTE)
    # =======================
    ranking = linear_fitness_ranking(UkPop, fitness, MaxF, MinF)
    TempPop = Populasi.copy()

    # Elitisme
    TempPop[0] = Populasi[idx_best].copy()

    # =======================
    # PROSES GENERASI BARU
    # =======================
    for j in range(1, UkPop, 2):

        # Roulette Wheel memilih dua induk
        p1 = roulette_wheel(UkPop, ranking)
        p2 = roulette_wheel(UkPop, ranking)

        parent1 = Populasi[p1]
        parent2 = Populasi[p2]

        # Crossover
        if np.random.rand() <= Psilang:
            anak1, anak2 = pindah_silang(parent1, parent2)
        else:
            anak1 = parent1.copy()
            anak2 = parent2.copy()

        # Mutasi
        anak1 = mutasi(anak1, Pmutasi)
        anak2 = mutasi(anak2, Pmutasi)

        # Masukkan ke populasi baru
        TempPop[j] = anak1
        if j+1 < UkPop:
            TempPop[j+1] = anak2

    Populasi = TempPop.copy()

# END FOR


# ==============================
# SIMPAN MODEL TERBAIK
# ==============================
print("\nMenyimpan model terbaik...")

def convert_to_jsonable(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, (np.integer, np.floating)):
        return obj.item()
    if isinstance(obj, dict):
        return {k: convert_to_jsonable(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [convert_to_jsonable(v) for v in obj]
    return obj


best_model = dekodekan_kromosom(best_global_chrom, Nvar, Nbit, Ra, Rb)

with open("FFNN_terbaik.json", "w") as f:
    json.dump(convert_to_jsonable(best_model), f, indent=4)

print("Model terbaik disimpan ke FFNN_terbaik.json")

plt.ioff()
plt.show()