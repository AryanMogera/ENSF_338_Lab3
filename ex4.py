import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import time


# safety net for recursion depth limit
def quick_sort(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot = partition(arr, low, high)
            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# 3. Test the algorithm with inputs of increasing sizes to depict the correlation between increasing array size and the time taken.
# We will use a reversed sorted array to portray the worst-case complexity of the algorithm.
# We will also use the time module to quantify the time taken by the algorithm for each input size.

sizes = [10, 50, 100, 500, 1000, 2000, 5000] 

time_data = []

for size in sizes:
    arr = list(range(size, 0, -1))  # Generate a reversed sorted array to force worst-case complexity
    start_time = time.time()
    sorted_arr = quick_sort(arr)
    end_time = time.time()
    time_data.append(end_time - start_time)

# Plotting
x = sizes
y_time = time_data

# Interpolating function
f_time = interp1d(x, y_time, kind='cubic')

x_new = np.linspace(min(x), max(x), 500)

plt.figure(figsize=(10, 6))
plt.plot(x, y_time, 'o', label='Time taken')
plt.plot(x_new, f_time(x_new), '-', label='Interpolating function (Time taken)', color='blue')

plt.xlabel('Input Size')
plt.ylabel('Time (seconds)')
plt.title('QuickSort: Time taken by Input Size (Worst-case complexity)')
plt.legend()
plt.grid(True)
plt.show()
