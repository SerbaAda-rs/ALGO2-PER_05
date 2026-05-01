print("=== PENCARIAN LINEAR <Skala_N = 16>  ===")
print("=== Rahmadi - 552010125009 ===")



def linear_search(data, target):
    count = 0
    for i in range(len(data)):
        count += 1
        if data[i] == target:
            return i, count
    return -1, count

data = [12, 5, 8, 20, 3, 15, 7, 1, 9, 14, 2, 11, 6, 4, 10, 13]
print("data", data)
target = int(input("Masukkan angka yang dicari: "))


posisi, langkah = linear_search(data, target)


print("Posisi:", posisi)
print("Jumlah langkah:", langkah)


# MENCARI DATA = 4, POSISI KE = 0, JUMLAH LANGKAH = 1
# MENCARI DATA = 16, POSISI KE = 3, JUMLAH LANGKAH = 4
# MENCARI DATA = 90, POSISI = "DATA TIDAK DITEMUKAN", JUMLAH LANGKAH = 6