# Lab Journal 4 - Task 4: Advanced Programming Concepts
# Programming for Artificial Intelligence

import random
from datetime import datetime

def bubble_sort(arr):
    """Implement bubble sort algorithm"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    """Implement binary search algorithm"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def file_operations():
    """Demonstrate file operations"""
    filename = "sample_data.txt"
    
    # Write to file
    with open(filename, 'w') as f:
        f.write("Sample data for AI course\n")
        f.write("Programming fundamentals\n")
        f.write(f"Generated on: {datetime.now()}\n")
    
    # Read from file
    with open(filename, 'r') as f:
        content = f.read()
        print(f"File content:\n{content}")

def main():
    print("Lab Journal 4 - Task 4: Advanced Programming Concepts")
    
    # Sorting algorithm
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {numbers}")
    sorted_numbers = bubble_sort(numbers.copy())
    print(f"Sorted array: {sorted_numbers}")
    
    # Binary search
    target = 25
    index = binary_search(sorted_numbers, target)
    if index != -1:
        print(f"Found {target} at index {index}")
    else:
        print(f"{target} not found in array")
    
    # Random number generation
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print(f"Random numbers: {random_numbers}")
    
    # File operations
    file_operations()

if __name__ == "__main__":
    main()