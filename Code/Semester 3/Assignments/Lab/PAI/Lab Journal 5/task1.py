# Lab Journal 5 - Task 1: NumPy Arrays and Operations
# Programming for Artificial Intelligence

import numpy as np

def main():
    print("Lab Journal 5 - Task 1: NumPy Arrays and Operations")
    
    # Create NumPy arrays
    arr1 = np.array([1, 2, 3, 4, 5])
    arr2 = np.array([6, 7, 8, 9, 10])
    
    print(f"Array 1: {arr1}")
    print(f"Array 2: {arr2}")
    
    # Basic operations
    print(f"Addition: {arr1 + arr2}")
    print(f"Multiplication: {arr1 * arr2}")
    print(f"Dot product: {np.dot(arr1, arr2)}")
    
    # 2D array operations
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    
    print(f"Matrix 1:\n{matrix1}")
    print(f"Matrix 2:\n{matrix2}")
    print(f"Matrix multiplication:\n{np.matmul(matrix1, matrix2)}")
    
    # Statistical operations
    data = np.random.randint(1, 100, 20)
    print(f"Random data: {data}")
    print(f"Mean: {np.mean(data):.2f}")
    print(f"Standard deviation: {np.std(data):.2f}")
    print(f"Min: {np.min(data)}, Max: {np.max(data)}")
    
    # Array reshaping
    reshaped = data.reshape(4, 5)
    print(f"Reshaped array (4x5):\n{reshaped}")

if __name__ == "__main__":
    main()