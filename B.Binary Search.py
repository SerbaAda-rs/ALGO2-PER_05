print("=== Binary Search ===")
print("=== Rahmadi - 552010125009 ===")


def binary_search(data, target):
    low = 0
    high = len(data) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2

        if data[mid] == target:
            return mid, count
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, count

data = [4, 8, 15, 16, 23, 42]
print("Data:", data)
target = int(input("Masukkan angka yang dicari: "))

posisi, langkah = binary_search(data, target)

print("Posisi:", posisi)
print("Jumlah langkah:", langkah)


# Binary Search membutuhkan jumlah langkah yang lebih sedikit dibandingkan Linear Search.karena binary membagi ruang pencarian menjadi dua setiap iterasi sehingga lebih efisien terutama pada data yang besar dan terurut