def linear_search_all(arr, target):
    indices = [i for i in range(len(arr)) if arr[i] == target]  # Collect all matching indices
    return indices if indices else [-1]  # Return -1 if not found

# Test the function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search_all(test_list, 5)
print(f"Linear Search: Indices of 5 are {result}")

def binary_search_insertion(arr, target):
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid  # Target should be inserted at or before mid
    
    return left  # Return the correct insertion point

# Test the function
sorted_list = [1, 3, 5, 7, 9]
insertion_point = binary_search_insertion(sorted_list, 6)
print(f"Binary Search Insertion Point: {insertion_point}")

def linear_search_with_count(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons  # Return index and count
    return -1, comparisons  # Return -1 if not found

def binary_search_with_count(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]

lin_result, lin_comparisons = linear_search_with_count(sorted_list, 7)
bin_result, bin_comparisons = binary_search_with_count(sorted_list, 7)

print(f"Linear Search: Index={lin_result}, Comparisons={lin_comparisons}")
print(f"Binary Search: Index={bin_result}, Comparisons={bin_comparisons}")

import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Optimal jump step
    prev, comparisons = 0, 0

    # Jump forward until we find a block containing target or exceed list length
    while prev < n and arr[min(n - 1, prev + step)] < target:
        comparisons += 1
        prev += step

    # Perform linear search in the found block
    for i in range(prev, min(prev + step, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons  # Found target

    return -1, comparisons  # Target not found

# Test Jump Search
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
jump_result, jump_comparisons = jump_search(sorted_list, 7)

print(f"Jump Search: Index={jump_result}, Comparisons={jump_comparisons}")
