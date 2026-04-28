print("=== PROGRAM PENCARIAN LINEAR ===")
print("=== Rahmadi - 552010125009 ===")



def linear_search(data, target):
    count = 0
    for i in range(len(data)):
        count += 1
        if data[i] == target:
            return i, count
    return -1, count

data = [4, 8, 15, 16, 23, 42]
print("data", data)
target = int(input("Masukkan angka yang dicari: "))


posisi, langkah = linear_search(data, target)


print("Posisi:", posisi)
print("Jumlah langkah:", langkah)