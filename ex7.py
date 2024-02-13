import json
import time
import matplotlib.pyplot as plt

file_path = 'ex7tasks.json'
with open (file_path, "r") as file:
    
    ex7task = json.load(file)


def binary_search(arr, val, start, end, initial_midpoint):
    mid = initial_midpoint
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return mid

def time_binary_search(arr, val, start, end, initial_midpoint):
    start_time = time.time()
    result = binary_search(arr, val, start, end, initial_midpoint)
    end_time = time.time()
    return result, end_time - start_time

task_results = []

for task in ex7task:
    best_midpoint = None
    best_time = float('inf')
    
    for midpoint_candidate in range(len(ex7task)):
        _, execution_time = time_binary_search(ex7task, task, 0, len(ex7task) - 1, midpoint_candidate)
        
        if execution_time < best_time:
            best_time = execution_time
            best_midpoint = midpoint_candidate
    
    task_results.append((task, best_midpoint))


tasks, midpoints = zip(*task_results)

plt.scatter(tasks, midpoints, alpha=0.5)
plt.title('Chosen Midpoint for Each Task')
plt.xlabel('Task')
plt.ylabel('Chosen Midpoint')
plt.show()





