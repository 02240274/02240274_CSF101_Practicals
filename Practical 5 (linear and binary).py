import math
import time

def linear_search_all(arr, target):
    indices = []
    comparisons = 0
    for i, val in enumerate(arr):
        comparisons += 1
        if val == target:
            indices.append(i)
    return indices, comparisons

def binary_search_insertion_point(arr, target):
    low, high = 0, len(arr)
    comparisons = 0
    while low < high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low, comparisons

def jump_search(arr, target):
    length = len(arr)
    block_size = int(math.sqrt(length))
    comparisons = 0

    # Finding the block
    start = 0
    end = block_size
    while start < length and arr[min(end, length)-1] < target:
        comparisons += 1
        start = end
        end += block_size
        if start >= length:
            return -1, comparisons

    # Linear search within the block
    for i in range(start, min(end, length)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Function to test and compare performance
def compare_search_algorithms(arr, target):
    print("=== Search Performance Comparison ===")
    
    start = time.time()
    result, comp_linear = linear_search_all(arr, target)
    end = time.time()
    print(f"Linear Search: Indices={result}, Comparisons={comp_linear}, Time={end - start:.6f}s")

    start = time.time()
    index, comp_binary = binary_search_insertion_point(arr, target)
    end = time.time()
    print(f"Binary Insertion Point: Index={index}, Comparisons={comp_binary}, Time={end - start:.6f}s")

    start = time.time()
    index, comp_jump = jump_search(arr, target)
    end = time.time()
    print(f"Jump Search: Index={index}, Comparisons={comp_jump}, Time={end - start:.6f}s")

# Example usage
arr = sorted([1, 2, 4, 4, 4, 5, 6, 7, 8])
target = 4
compare_search_algorithms(arr, target)
