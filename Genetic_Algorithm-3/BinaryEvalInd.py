from math import exp,sqrt
from BangMatrixIT import BangMatrixIT
import random


def sigmoid(x, c):
    return 1.0 / (1.0 + exp(-c * x))

def BinaryEvalInd(FFNNstruk,JumMasukan,JPmasukan,IM,TM):
    c = 1.0
    n2 = JumMasukan**2

    Wih = []

    Wtemp = FFNNstruk[0:n2]

    for i in range(JumMasukan):
        Wih.append(Wtemp[i*JumMasukan:(i+1)*JumMasukan])

    bih = FFNNstruk[n2 : n2 + JumMasukan]                        # panjang JumMasukan
    Who = FFNNstruk[n2 + JumMasukan : n2 + 2 * JumMasukan]      # panjang JumMasukan
    bho_index = (JumMasukan + 1) ** 2 - 1                        # MATLAB (JumMasukan+1)^2 -> 1-based
    bho = FFNNstruk[bho_index]

    RMSE = 0.0

    # Loop evaluasi untuk setiap pola
    for evaluasi in range(JPmasukan):
        # Hitung aktivasi hidden Xih (panjang JumMasukan)
        Xih = [0.0] * JumMasukan
        for i in range(JumMasukan):
            SumWlb = 0.0
            for j in range(JumMasukan):
                # tambah Wih(i,j)*IM(evaluasi,j) + bih(j)
                SumWlb += (Wih[i][j] * IM[evaluasi][j] + bih[j])
            Xih[i] = sigmoid(SumWlb, c)

        # Hitung output (single neuron)
        SumWXb = 0.0
        for j in range(JumMasukan):
            SumWXb += (Who[j] * Xih[j] + bho)

        Xho = sigmoid(SumWXb, c)

        # Akumulasi kuadrat error
        RMSE += (TM[evaluasi] - Xho) ** 2

    # Delta dan fitness sesuai rumus gambar
    Delta = sqrt((1.0 / JPmasukan) * RMSE)

    # Hindari pembagian dengan nol
    if Delta == 0:
        fitness = float('inf')
    else:
        fitness = 1.0 / Delta

    return fitness

if __name__ == "__main__":
    JumMasukan = 3
    JPmasukan = 2 ** JumMasukan  # 8
    IM, TM = BangMatrixIT(JumMasukan, JPmasukan)

    # Contoh FFNNstruk sesuai penjelasan: panjang 16 (untuk JumMasukan=3)
    # Kita buat random sebagai contoh (bisa diganti dengan vektor nyata)
    FFNNstruk = [random.uniform(-1, 1) for _ in range(16)]

    fitness = BinaryEvalInd(FFNNstruk, JumMasukan, JPmasukan, IM, TM)
    print("fitness =", fitness)