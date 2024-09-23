def selection_sort(arr):
    # Loop melalui seluruh elemen array
    for i in range(len(arr)):
        # Temukan elemen terkecil di sisa array yang belum terurut
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Tukar elemen terkecil dengan elemen pertama di bagian yang belum terurut
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Contoh penggunaan
arr = [64, 25, 12, 22, 11, 90, 66, 64]
print("Array sebelum diurutkan:", arr)

selection_sort(arr)
print("Array setelah diurutkan:", arr)
