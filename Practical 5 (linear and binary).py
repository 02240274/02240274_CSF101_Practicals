def linear_search_all(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

def binary_search_insertion_point(arr, target):
    low = 0
    high = len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

def linear_search_with_comparisons(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

def binary_search_with_comparisons(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

import math

def jump_search_with_comparisons(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    comparisons = 0

    # Finding the block
    while prev < n and arr[min(step, n) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1, comparisons

    # Linear search in the block
    while prev < min(step, n):
        comparisons += 1
        if arr[prev] == target:
            return prev, comparisons
        prev += 1

    return -1, comparisons

def compare_searches(arr, target):
    print("Linear Search:", linear_search_with_comparisons(arr, target))
    print("Binary Search:", binary_search_with_comparisons(arr, target))
    print("Jump Search:", jump_search_with_comparisons(arr, target))
