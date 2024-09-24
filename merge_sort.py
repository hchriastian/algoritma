def merge_sort(arr):
    if len(arr) > 1:
        # Menentukan titik tengah array
        mid = len(arr) // 2
        
        # Membagi array menjadi dua bagian
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Rekursif memanggil merge_sort pada kedua bagian
        merge_sort(left_half)
        merge_sort(right_half)
        
        # Inisialisasi indeks untuk penggabungan
        i = j = k = 0
        
        # Menggabungkan kedua bagian yang telah diurutkan
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Memasukkan sisa elemen dari left_half jika ada
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        # Memasukkan sisa elemen dari right_half jika ada
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Contoh penggunaan
arr = [38, 27, 43, 3, 9, 82, 10]
print("Array sebelum diurutkan:", arr)
merge_sort(arr)
print("Array setelah diurutkan:", arr)
