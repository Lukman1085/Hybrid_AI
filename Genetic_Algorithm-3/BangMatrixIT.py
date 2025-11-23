from Int2Bin import Int2Bin

def BangMatrixIT(JumMasukan,JPmasukan):
    IM = []
    TM = [0] * JPmasukan

    for i in range(JPmasukan):
        row = Int2Bin(i, JumMasukan)
        IM.append(row)
        
        if sum(row) % 2 == 1:
            TM[i] = 1
        else:
            TM[i] = 0
    return IM, TM

if __name__ == '__main__':
    IM, TM = BangMatrixIT(4, 8)

    print("IM:")
    for r in IM:
        print(r)

    print("TM:", TM)
        