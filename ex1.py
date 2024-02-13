''' 2. Since the merge sort algorithm below is using the divide and conquer strategy, it will do so
recursicely till it reaches only one element in the array. This will take a total time of O(logn). After the
recursion, the merge function will take O(n) time to merge the two arrays. Therefore, the total time taken will be the worst-case time complexity of O(nlogn).

'''


import sys 

sys.setrecursionlimit(200000)

def merge_sort(arr, low, high):
      if low < high:
          mid = (low + high) // 2
          merge_sort(arr, low, mid)
          merge_sort(arr, mid + 1, high)
          merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left = arr[low:mid + 1]
    right = arr[mid + 1:high + 1]
    left.append(float('inf'))
    right.append(float('inf'))
    i = j = 0
    for k in range(low, high + 1):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

a=[8,42,25,3,3,2,27,3]

merge_sort(a,0,len(a)-1)
print(a)