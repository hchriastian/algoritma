def insertion_sort(arr):
    # Loop dari elemen kedua hingga elemen terakhir
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Pindahkan elemen yang lebih besar dari 'key' satu posisi ke depan
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Masukkan 'key' ke posisi yang benar
        arr[j + 1] = key

# Contoh penggunaan
arr = [12, 11, 13, 5, 6]
print("Array sebelum diurutkan:", arr)

insertion_sort(arr)
print("Array setelah diurutkan:", arr)
