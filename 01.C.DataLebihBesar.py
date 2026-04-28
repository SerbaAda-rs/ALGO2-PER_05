import os
import subprocess
import time

def clear():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

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


riwayat = []

while True:
    print("\n=== Binary Search Data Lebih Besar ===")
    print("=== Rahmadi - 552010125009 ===\n")

    # tampilkan riwayat dulu
    print("==== Riwayat Pencarian ====")
    if len(riwayat) == 0:
        print("Belum ada pencarian")
    else:
        for r in riwayat:
            print(r)

    # data genap
    data = list(range(1, 1001))
    print("\nData:", data)

    try:
        target = int(input("\nMasukkan angka yang dicari: "))
    except ValueError:
        print("Input harus berupa angka!")
        time.sleep(2)
        continue

    posisi, langkah = binary_search(data, target)

    # simpan hasil ke riwayat
    if posisi != -1:
        hasil = f"Target {target} ditemukan di posisi {posisi} (langkah: {langkah})"
    else:
        hasil = f"Target {target} tidak ditemukan (langkah: {langkah})"

    print(hasil)
    riwayat.append(hasil) 

    ulang = input("\nIngin mencari lagi? (y/n): ").lower()
    if ulang != 'y':
        print("Program selesai.")
        break


# Binary Search jauh lebih efisien dibanding Linear Search karena membagi data setiap langkah, sehingga jumlah langkahnya jauh lebih sedikit. Ini menunjukkan keunggulan kompleksitas O(log n) dibanding O(n).