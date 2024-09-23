def merge_sort(arr):
    if len(arr) > 1:
        # Membagi array menjadi dua bagian
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Mengurutkan setiap bagian secara rekursif
        merge_sort(left_half)
        merge_sort(right_half)

        # Variabel indeks untuk subarray dan array utama
        i = j = k = 0

        # Menggabungkan kembali dua bagian yang terurut
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Menambahkan sisa elemen di left_half, jika ada
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Menambahkan sisa elemen di right_half, jika ada
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Contoh penggunaan
arr = [38, 27, 43, 3, 9, 82, 10]
print("Array sebelum diurutkan:", arr)

merge_sort(arr)
print("Array setelah diurutkan:", arr)
