def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def hybrid_quick_sort(arr, low=0, high=None, threshold=10):
    if high is None:
        high = len(arr) - 1

    while low < high:
        if high - low + 1 < threshold:
            insertion_sort(arr, low, high)
            break
        else:
            pi = partition(arr, low, high)
            if pi - low < high - pi:
                hybrid_quick_sort(arr, low, pi - 1, threshold)
                low = pi + 1
            else:
                hybrid_quick_sort(arr, pi + 1, high, threshold)
                high = pi - 1

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

def bubble_sort_visual(arr, bar_rects, text):
    def update(frame):
        nonlocal arr
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr

    def draw(arr):
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
        text.set_text("Sorting...")

    generator = update(0)
    
    def animate(frame):
        try:
            current_arr = next(generator)
            draw(current_arr)
        except StopIteration:
            text.set_text("Done!")

    return animate

# Setup
def run_bubble_sort_visual():
    arr = [random.randint(1, 100) for _ in range(50)]
    fig, ax = plt.subplots()
    bar_rects = plt.bar(range(len(arr)), arr, align="edge")
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    ax.set_title("Bubble Sort Visualization")

    anim = animation.FuncAnimation(fig, bubble_sort_visual(arr, bar_rects, text), interval=50)
    plt.show()

# To run:
# run_bubble_sort_visual()
