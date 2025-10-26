import pandas as pd
import matplotlib.pyplot as plt

# === 1️⃣ Baca data CSV ===
# Ganti path sesuai lokasi file kamu
data = pd.read_csv("hasil_generasi.csv")

data['Rata_Rata_Generasi'] = data.groupby('Laju_Mutasi')['Generasi_Solusi'].transform('mean')
data = data[['Laju_Mutasi', 'Rata_Rata_Generasi']]

# Pastikan nama kolom sesuai
if not {'Laju_Mutasi', 'Rata_Rata_Generasi'}.issubset(data.columns):
    raise ValueError("CSV harus memiliki kolom: Laju_Mutasi dan Rata_Rata_Generasi")

# === 2️⃣ Urutkan data berdasarkan Laju_Mutasi ===
data = data.sort_values(by="Laju_Mutasi")

# === 3️⃣ Buat grafik ===
plt.figure(figsize=(8, 5))
plt.plot(
    data["Laju_Mutasi"],
    data["Rata_Rata_Generasi"],
    marker="o",
    linestyle="-",
    linewidth=2,
    markersize=6
)

# === 4️⃣ Pengaturan tampilan ===
plt.title("Hubungan antara Laju Mutasi dan Rata-rata Generasi", fontsize=13)
plt.xlabel("Laju Mutasi", fontsize=12)
plt.ylabel("Rata-rata Generasi Hingga Solusi", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

# === 5️⃣ Tampilkan grafik ===
plt.show()
