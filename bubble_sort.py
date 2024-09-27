def bubble_sort(arr):
    n = len(arr)
    
    # Loop untuk setiap elemen array
    for i in range(n):
        # Flag untuk mengecek apakah ada swap yang dilakukan
        swapped = False
        
        # Loop untuk membandingkan elemen berpasangan
        for j in range(0, n - i - 1):
            # Jika elemen lebih besar dari elemen berikutnya, tukar posisi
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # Jika tidak ada swap yang dilakukan, berarti array sudah terurut
        if not swapped:
            break

# Contoh penggunaan
arr = [64, 34, 25, 12, 22, 20, 90, 88, 55]
print("Array sebelum diurutkan:", arr)

bubble_sort(arr)
print("Array setelah diurutkan:", arr)
