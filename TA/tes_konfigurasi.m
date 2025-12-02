clear; clc;

JumlahEksperimen = 20; 
DataGen = zeros(1, JumlahEksperimen);
DataFitness = zeros(1, JumlahEksperimen);
WaktuMulai = tic;

fprintf('Sedang menjalankan %d eksperimen. Mohon tunggu...\n', JumlahEksperimen);

for i = 1:JumlahEksperimen
    % Panggil fungsi GA yang sudah dioptimasi (lihat Langkah 3)
    [GenSelesai, FitAkhir] = Copy_of_FFNNBinaryLatih();
    
    DataGen(i) = GenSelesai;
    DataFitness(i) = FitAkhir;
    
    % Tampilkan progress bar sederhana
    fprintf('.'); 
    if mod(i, 5) == 0, fprintf(' (%d/%d)\n', i, JumlahEksperimen); end
end

WaktuTotal = toc(WaktuMulai);

% --- HITUNG STATISTIK ---
MinGen = min(DataGen);
MaxGen = max(DataGen);
RataGen = mean(DataGen);
StdGen = std(DataGen);
SuccessRate = sum(DataGen < 100) / JumlahEksperimen; % Asumsi MaxG = 100

fprintf('\n--- HASIL EKSPERIMEN ---\n');
fprintf('Total Waktu Eksekusi : %.2f detik\n', WaktuTotal);
fprintf('Rata-rata Generasi   : %.2f\n', RataGen);
fprintf('Generasi Tercepat    : %d\n', MinGen);
fprintf('Generasi Terlambat   : %d\n', MaxGen);
fprintf('Stabilitas (Std Dev) : %.2f\n', StdGen);
fprintf('Success Rate (100 generasi) : %f\n', SuccessRate);
fprintf('Rata-rata Fitness    : %f\n', mean(DataFitness));

% --- VISUALISASI DISTRIBUSI ---

figure('Name', 'Analisis Distribusi Generasi', 'Color', 'w');

% 1. Buat Histogram
h = histogram(DataGen, 10); % Membagi data menjadi 10 bin (kelompok)
h.FaceColor = [0.2 0.6 0.8]; % Warna biru yang rapi
h.EdgeColor = 'w';
hold on;

% 2. Garis Rata-rata (Mean) - Merah Putus-putus
GarisRata = xline(RataGen, '--r', sprintf('Rata-rata: %.1f', RataGen));
GarisRata.LineWidth = 2;
GarisRata.LabelVerticalAlignment = 'top';

% 3. Label dan Judul
title('Distribusi Kecepatan Konvergensi GA', 'FontSize', 12);
xlabel('Generasi ke- (Saat Solusi Ditemukan)', 'FontSize', 10);
ylabel('Frekuensi (Jumlah Percobaan)', 'FontSize', 10);
grid on;
grid minor;

% 4. Menandai Batas Maksimum (Jika ada yang gagal)
if max(DataGen) >= 100
    xline(100, '-k', 'Max Gen (Gagal/Stop)', 'LabelHorizontalAlignment', 'left');
end

hold off;