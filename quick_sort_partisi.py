def partition(arr, low, high):
    # Memilih elemen terakhir sebagai pivot
    pivot = arr[high]
    i = low - 1  # Indeks dari elemen yang lebih kecil

    # Loop melalui array dari low hingga high-1
    for j in range(low, high):
        # Jika elemen saat ini lebih kecil atau sama dengan pivot
        if arr[j] <= pivot:
            i += 1  # Pindahkan batas elemen yang lebih kecil
            arr[i], arr[j] = arr[j], arr[i]  # Tukar elemen yang lebih kecil dengan elemen saat ini

    # Tukar pivot dengan elemen di posisi i+1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1  # Kembalikan posisi pivot

def quick_sort(arr, low, high):
    if low < high:
        # pi adalah indeks pivot setelah partisi
        pi = partition(arr, low, high)

        # Urutkan bagian kiri dan kanan dari pivot
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Contoh penggunaan
arr = [10, 80, 30, 90, 20, 50, 70]
print("Array sebelum diurutkan:", arr)

quick_sort(arr, 0, len(arr) - 1)
print("Array setelah diurutkan:", arr)
