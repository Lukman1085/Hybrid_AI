def Int2Bin(BilInteger, JumBit):
    BilBiner = bin(BilInteger)[2:]
    BilBiner = BilBiner.zfill(JumBit)
    return [int(x) for x in BilBiner]

    
if __name__ == "__main__":
    tes = Int2Bin(33,5)
    print(tes)

  