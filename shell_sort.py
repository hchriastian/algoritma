def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inisialisasi gap (jarak) dengan setengah panjang array
    
    # Loop selama gap lebih besar dari 0
    while gap > 0:
        # Loop untuk tiap elemen dari gap hingga akhir array
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Geser elemen array dengan jarak gap ke posisi yang benar
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # Tempatkan elemen temp pada posisi yang benar
            arr[j] = temp
        
        # Kurangi gap menjadi setengahnya
        gap //= 2

# Contoh penggunaan
arr = [12, 34, 54, 2, 3]
print("Array sebelum diurutkan:", arr)

shell_sort(arr)
print("Array setelah diurutkan:", arr)
