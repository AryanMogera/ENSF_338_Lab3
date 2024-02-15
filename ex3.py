import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import random

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return comparisons, swaps

# Testing the algorithm with inputs of increasing size so it depicts the correlation between increasing array size and the number of comparisons and swaps.
# We will use a reversed sorted array to portray the worst-case complexity of the algorithm.
# We will also use the random module to shuffle the array to simulate average-case complexity as suggested in the exercise. 

sizes = [100, 500, 1000, 2000, 5000, 10000]  

comparison_data = []
swap_data = []

for size in sizes:
    arr = list(range(size))  

    random.shuffle(arr)  # Shuffle the array to simulate average-case scenario as suggested in the exercise
    comparisons, swaps = bubble_sort(arr.copy())
    comparison_data.append(comparisons)
    swap_data.append(swaps)


x = sizes
y_comparisons = comparison_data
y_swaps = swap_data


# Interpolating functions for comparisons and swaps

f_comparisons = interp1d(x, y_comparisons, kind='cubic')
f_swaps = interp1d(x, y_swaps, kind='cubic')

x_new = np.linspace(min(x), max(x), 500)

plt.figure(figsize=(10, 6))
plt.plot(x, y_comparisons, 'o', label='Comparisons')
plt.plot(x_new, f_comparisons(x_new), '-', label='Interpolating function (Comparisons)', color='blue')

plt.plot(x, y_swaps, 'o', label='Swaps')
plt.plot(x_new, f_swaps(x_new), '-', label='Interpolating function (Swaps)', color='orange')

plt.xlabel('Input Size')
plt.ylabel('Count')
plt.title('Bubble Sort: Comparisons and Swaps by Input Size')
plt.legend()
plt.grid(True)
plt.show()
