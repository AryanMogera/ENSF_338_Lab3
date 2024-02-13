#4 Binary insertion sort algorithm was faster because it is more efficient due to its reduced number 
#of comparisons compared to standard insertion sort, especially when dealing eith large datasets

import time
import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def binary_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to run the experiment
def run_experiment(sort_function, input_size):
    random_list = [random.randint(1, 1000) for _ in range(input_size)]

    start_time = time.time()
    sorted_list = sort_function(random_list)
    end_time = time.time()

    elapsed_time = end_time - start_time
    return elapsed_time

def plot_results(input_sizes, binary_times, insertion_times):
    xnew = np.linspace(min(input_sizes), max(input_sizes), 300)

    # Interpolating functions
    spl_binary = make_interp_spline(input_sizes, binary_times, k=3)
    y_binary = spl_binary(xnew)

    spl_insertion = make_interp_spline(input_sizes, insertion_times, k=3)
    y_insertion = spl_insertion(xnew)

    # Plotting
    plt.plot(xnew, y_binary, label='Binary Insertion Sort', color='blue')
    plt.plot(xnew, y_insertion, label='Standard Insertion Sort', color='green')

    plt.scatter(input_sizes, binary_times, color='blue')
    plt.scatter(input_sizes, insertion_times, color='green')

    plt.xlabel('Input Size')
    plt.ylabel('Time Taken (seconds)')
    plt.title('Comparison of Binary and Standard Insertion Sort')
    plt.legend()
    plt.show()

# Experiment parameters
input_sizes = [100, 500, 1000, 2000, 5000]

# Run experiments and collect times
binary_times = [run_experiment(binary_sort, size) for size in input_sizes]
insertion_times = [run_experiment(insertion_sort, size) for size in input_sizes]

# Plot results
plot_results(input_sizes, binary_times, insertion_times)


