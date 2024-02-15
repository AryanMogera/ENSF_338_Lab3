import matplotlib.pyplot as plt
import numpy as np
import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # No swaps; array is sorted
            break
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Randomized pivot selection
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

def generate_sorted_array(size):
    return list(range(1, size + 1))

def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))

def measure_sorting_time(sorting_function, arr):
    start_time = time.time()
    sorting_function(arr)
    end_time = time.time()
    return end_time - start_time

array_sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000]
times_bubble_random = []
times_quicksort_random = []
times_bubble_best = []
times_quicksort_best = []
times_bubble_worst = []
times_quicksort_worst = []

for size in array_sizes:
    arr_random = generate_random_array(size)
    arr_sorted = generate_sorted_array(size)
    arr_reverse_sorted = generate_reverse_sorted_array(size)
    
    times_bubble_random.append(measure_sorting_time(bubble_sort, arr_random.copy()))
    times_quicksort_random.append(measure_sorting_time(quicksort, arr_random.copy()))
    
    times_bubble_best.append(measure_sorting_time(bubble_sort, arr_sorted.copy()))
    times_quicksort_best.append(measure_sorting_time(quicksort, arr_sorted.copy()))
    
    times_bubble_worst.append(measure_sorting_time(bubble_sort, arr_reverse_sorted.copy()))
    times_quicksort_worst.append(measure_sorting_time(quicksort, arr_reverse_sorted.copy()))

# Plotting with adjusted layout
fig, axs = plt.subplots(3, 1, figsize=(12, 18), sharex=True)

axs[0].plot(array_sizes, times_bubble_random, label='Bubble Sort - Average', marker='o', linestyle='-', linewidth=1, markersize=5)
axs[0].plot(array_sizes, times_quicksort_random, label='Quicksort - Average', marker='x', linestyle='-', linewidth=1, markersize=5)
axs[0].set_title('Average Case Performance')
axs[0].set_ylabel('Time (seconds)')
axs[0].legend()

axs[1].plot(array_sizes, times_bubble_best, label='Bubble Sort - Best', marker='o', linestyle='-', linewidth=1, markersize=5)
axs[1].plot(array_sizes, times_quicksort_best, label='Quicksort - Best', marker='x', linestyle='-', linewidth=1, markersize=5)
axs[1].set_title('Best Case Performance')
axs[1].set_ylabel('Time (seconds)')
axs[1].legend()

axs[2].plot(array_sizes, times_bubble_worst, label='Bubble Sort - Worst', marker='o', linestyle='-', linewidth=1, markersize=5)
axs[2].plot(array_sizes, times_quicksort_worst, label='Quicksort - Worst', marker='x', linestyle='-', linewidth=1, markersize=5)
axs[2].set_title('Worst Case Performance')
axs[2].set_xlabel('Array Size')
axs[2].set_ylabel('Time (seconds)')
axs[2].legend()

plt.tight_layout()
plt.show()
