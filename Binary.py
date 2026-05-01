print("=== Binary Search <Skala_N = 16> ===")
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

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
print("Data:", data)
target = int(input("Masukkan angka yang dicari: "))

posisi, langkah = binary_search(data, target)

print("Posisi:", posisi)
print("Jumlah langkah:", langkah)


# Binary Search membutuhkan jumlah langkah yang lebih sedikit dibandingkan Linear Search.karena binary membagi ruang pencarian menjadi dua setiap iterasi sehingga lebih efisien terutama pada data yang besar dan terurut