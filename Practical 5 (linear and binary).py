# Linear search: Modified to return all indices where the target appears
def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices  # Return all indices where target is found

# Binary search: Finds the insertion point for a target value in a sorted list
def binary_search_insertion(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low  # This is the insertion point for the target

# Count comparisons in Linear Search
def linear_search_count(arr, target):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == target:
            return count  # Return the count when target is found
    return count  # If target isn't found, return the count

# Count comparisons in Binary Search
def binary_search_count(arr, target):
    low, high = 0, len(arr)
    count = 0
    while low < high:
        count += 1
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return count  # Return the number of comparisons made

# Jump Search Algorithm
import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))  # Calculate step size
    prev = 0
    # Jumping in steps of 'step' until we find a block where target could be
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:  # If we go out of bounds, the target isn't in the list
            return -1
    # Perform a linear search within the block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i  # Return index of target
    return -1  # If target isn't found

# Count comparisons in Jump Search
def jump_search_count(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    count = 0
    while arr[min(step, n)-1] < target:
        prev = step
        step += int(math.sqrt(n))
        count += 1  # Each jump is a comparison
        if prev >= n:
            return count
    for i in range(prev, min(step, n)):
        count += 1
        if arr[i] == target:
            return count  # Return the comparison count when target is found
    return count  # If target isn't found, return the count

# Example usage:

arr = [1, 2, 2, 2, 3, 4, 5, 6]
target = 2

# Linear Search
print("Linear Search indices:", linear_search(arr, target))  # Output: [1, 2, 3]
print("Linear Search Comparison Count:", linear_search_count(arr, target))  # Output: Comparisons made

# Binary Search Insertion
sorted_arr = sorted(arr)  # Binary search requires a sorted list
print("Binary Search Insertion Point:", binary_search_insertion(sorted_arr, target))  # Output: 2

# Binary Search Count
print("Binary Search Comparison Count:", binary_search_count(sorted_arr, target))  # Output: Comparisons made

# Jump Search
print("Jump Search Index:", jump_search(arr, target))  # Output: 1
print("Jump Search Comparison Count:", jump_search_count(arr, target))  # Output: Comparisons made
