def heapify(arr, n, i):
    largest = i      # Inisialisasi elemen terbesar sebagai root
    left = 2 * i + 1 # Indeks anak kiri
    right = 2 * i + 2 # Indeks anak kanan

    # Jika anak kiri lebih besar dari root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Jika anak kanan lebih besar dari elemen terbesar sementara
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Jika elemen terbesar bukan root, tukar dan heapify subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Rekursif heapify

def heap_sort(arr):
    n = len(arr)

    # Membangun max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Ekstraksi elemen satu per satu dari heap
    for i in range(n-1, 0, -1):
        # Pindahkan root (elemen terbesar) ke akhir array
        arr[i], arr[0] = arr[0], arr[i]
        # Heapify heap yang tersisa
        heapify(arr, i, 0)

# Contoh penggunaan
arr = [12, 11, 13, 5, 6, 7]
print("Array sebelum diurutkan:", arr)

heap_sort(arr)
print("Array setelah diurutkan:", arr)
