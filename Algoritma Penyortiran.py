import time
import random

# Fungsi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Fungsi Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Fungsi Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Fungsi Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Membuat array random dengan 10000 elemen
array = random.sample(range(1, 100000), 10000)

# Mengukur waktu untuk setiap metode sorting

# Bubble Sort
arr_bubble = array.copy()
start_time = time.time()
bubble_sort(arr_bubble)
bubble_time = time.time() - start_time

# Selection Sort
arr_selection = array.copy()
start_time = time.time()
selection_sort(arr_selection)
selection_time = time.time() - start_time

# Insertion Sort
arr_insertion = array.copy()
start_time = time.time()
insertion_sort(arr_insertion)
insertion_time = time.time() - start_time

# Shell Sort
arr_shell = array.copy()
start_time = time.time()
shell_sort(arr_shell)
shell_time = time.time() - start_time

# Menampilkan hasil
print("Array Awal (10000 elemen acak):", array)
print("\nWaktu Bubble Sort: %s detik" % bubble_time)
print("\nWaktu Selection Sort: %s detik" % selection_time)
print("\nWaktu Insertion Sort: %s detik" % insertion_time)
print("\nWaktu Shell Sort: %s detik" % shell_time)