def partition(arr, low, high):
    # Memilih elemen terakhir sebagai pivot
    pivot = arr[high]
    i = low - 1  # Indeks elemen yang lebih kecil

    for j in range(low, high):
        # Jika elemen saat ini lebih kecil atau sama dengan pivot
        if arr[j] <= pivot:
            i += 1  # Pindahkan indeks elemen yang lebih kecil
            arr[i], arr[j] = arr[j], arr[i]  # Tukar elemen

    # Tempatkan pivot di posisi yang benar
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Kembalikan indeks pivot

def quick_sort(arr, low, high):
    if low < high:
        # Temukan pivot setelah pengaturan partisi
        pi = partition(arr, low, high)

        # Rekursif quicksort untuk elemen di kiri pivot
        quick_sort(arr, low, pi - 1)
        # Rekursif quicksort untuk elemen di kanan pivot
        quick_sort(arr, pi + 1, high)

# Contoh penggunaan
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("Array sebelum diurutkan:", arr)

quick_sort(arr, 0, n - 1)
print("Array setelah diurutkan:", arr)
