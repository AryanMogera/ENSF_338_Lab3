
import sys 
import random
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

def measure_performance_random():

    arr = [i for i in range(100)]
    random.shuffle(arr)


    linear_search_time = timeit.timeit(lambda: linear_search(arr, random.choice(arr)), number=100)


    quick_sort_time = timeit.timeit(lambda: quick_sort(arr, 0, len(arr) - 1), number=100)


    print("Linear Search Time for Random element:", linear_search_time)
    print("Quick Sort Time for Random elemet: ", quick_sort_time)
    print("\n")

measure_performance_random()

def measure_performance(input_sizes):
    linear_search_times = []
    quick_sort_times = []
    for size in input_sizes:
        arr = [i for i in range(size)]
        random.shuffle(arr)
        
        linear_search_time = timeit.timeit(lambda: linear_search(arr, random.choice(arr)), number=100)
        quick_sort_time = timeit.timeit(lambda: quick_sort(arr, 0, len(arr) - 1), number=100)
        
        linear_search_times.append(linear_search_time)
        quick_sort_times.append(quick_sort_time)
        
    return linear_search_times, quick_sort_times

input_sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]

linear_search_times, quick_sort_times = measure_performance(input_sizes)

# Plotting
plt.plot(input_sizes, linear_search_times, label='Linear Search')
plt.plot(input_sizes, quick_sort_times, label='Quick Sort')
plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('Performance of Linear Search vs Quick Sort')
plt.legend()
plt.show()

"""In the graph, we can see that the time taken by linear search and quick sort increases as the input size increases. However, 
the time taken by quick sort increases at a much faster rate than linear search. This is because the time complexity of quick sort is O(n^2) in the worst case, 
while the time complexity of linear search is O(n). Therefore, quick sort is much slower than linear search for large input sizes."""