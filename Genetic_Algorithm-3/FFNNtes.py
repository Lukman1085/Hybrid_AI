
import numpy as np
import json

with open("FFNN_terbaik.json","r") as f:
    model = json.load(f)

def decodeModelFFNN(data):
    n = 3
    input_dim = 3

    # Decode sama seperti MATLAB
    Wih = np.array(data[0 : n*input_dim]).reshape(n, input_dim)
    bih = np.array(data[n*input_dim : n*input_dim + n])
    Who = np.array(data[n*input_dim + n : n*input_dim + n + n])
    bho = data[-1]

    model = {
        "Wih": Wih.tolist(),
        "bih": bih.tolist(),
        "Who": Who.tolist(),
        "bho": bho,
        "c": 1
    }
    return model





def sigmoid(x, c=1):
    return 1 / (1 + np.exp(-c * x))

def ffnn_predict(model, x_input):
    """
    model: dict dengan kunci:
        - 'Wih' : bobot input → hidden (n x 3)
        - 'bih' : bias hidden (n)
        - 'Who' : bobot hidden → output (n)
        - 'bho' : bias output (scalar)
        - 'c'   : konstanta sigmoid
        
    x_input: array/list panjang 3
    """

    x = np.array(x_input).astype(float)  # 3 input

    Wih = np.array(model["Wih"])
    bih = np.array(model["bih"])
    Who = np.array(model["Who"])
    bho = float(model["bho"])
    c   = float(model.get("c", 1))  # default 1 kalau tidak ada

    # --- Hidden layer ---
    # SumWlb(ii) = Σ (Wih(ii,jj) * IM(jj)) + bih(ii)
    sum_hidden = Wih @ x + bih
    Xih = sigmoid(sum_hidden, c)

    # --- Output layer ---
    sum_output = np.dot(Who, Xih) + bho
    Xho = sigmoid(sum_output, c)

    return Xho

def test_interaktif(model):
    while True:
        print("\nPengujian FFNN")
        print("Masukkan tiga input biner untuk FFNN:")

        x1 = float(input("X1: "))
        x2 = float(input("X2: "))
        x3 = float(input("X3: "))

        out = ffnn_predict(model, [x1, x2, x3])
        print(f"\nOutput FFNN = {out:.6f}")

        ulang = input("Tes lagi? (y/n): ").lower()
        if ulang != 'y':
            break

if __name__ == "__main__":
    model = decodeModelFFNN(model)
    test_interaktif(model)