import time
import random

# Fungsi Heap Sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Fungsi Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Fungsi Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Membuat array random dengan 10.000 elemen
array = random.sample(range(1, 100000), 10000)

# Heap Sort
arr_heap = array.copy()
start_time = time.time()
heap_sort(arr_heap)
heap_time = time.time() - start_time

# Merge Sort
arr_merge = array.copy()
start_time = time.time()
merge_sort(arr_merge)
merge_time = time.time() - start_time

# Quick Sort
arr_quick = array.copy()
start_time = time.time()
arr_quick_sorted = quick_sort(arr_quick)
quick_time = time.time() - start_time

# Menampilkan hasil
print("Array Awal (10000 elemen acak):", array)
print("Waktu Heap Sort: %s detik" % heap_time)
print("Waktu Merge Sort: %s detik" % merge_time)
print("Waktu Quick Sort: %s detik" % quick_time)