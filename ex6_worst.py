import random
import sys
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(200000)

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def measure_performance(input_sizes):
    linear_search_times = []
    quick_sort_times = []
    for size in input_sizes:
        arr = [i for i in range(size)]
        # Shuffle the array to avoid the best-case scenario
        random.shuffle(arr)

        arr.sort()  # This will cause quicksort to incur worst-case performance

        linear_search_time = timeit.timeit(lambda: linear_search(arr, random.choice(arr)), number=100)
        quick_sort_time = timeit.timeit(lambda: quick_sort(arr, 0, len(arr) - 1), number=100)
        
        linear_search_times.append(linear_search_time)
        quick_sort_times.append(quick_sort_time)
        
    return linear_search_times, quick_sort_times


input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

linear_search_times, quick_sort_times = measure_performance(input_sizes)


plt.plot(input_sizes, linear_search_times, label='Linear Search')
plt.plot(input_sizes, quick_sort_times, label='Quick Sort (Worst Case)')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Performance of Linear Search vs Quick Sort (Worst Case)')
plt.legend()
plt.show()
