from simpleGA import simpleGA
import csv

target = "andi lukman"
besar_populasi = 10
laju_mutasi_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

jumlah_run = 10000  # misalnya setiap laju mutasi diuji 10000x

hasil_generasi = []

for laju_mutasi in laju_mutasi_list:
    for i in range(jumlah_run):
        _, gen_solve = simpleGA(target, besar_populasi, laju_mutasi)
        hasil_generasi.append({
            "Run": i + 1,
            "Laju_Mutasi": laju_mutasi,
            "Generasi_Solusi": gen_solve
        })
        print(f"Mutasi {laju_mutasi:.1f} | Run {i+1} | Generasi: {gen_solve}")

# Simpan ke CSV
with open("hasil_generasi.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Run", "Laju_Mutasi", "Generasi_Solusi"])
    writer.writeheader()
    writer.writerows(hasil_generasi)

print("\n✅ Semua hasil eksperimen tersimpan di 'hasil_generasi.csv'")
