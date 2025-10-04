# Lab Journal 4 - Task 1: Python Fundamentals and Basic Operations
# Programming for Artificial Intelligence

# Basic Python operations and data types
def main():
    print("Lab Journal 4 - Task 1: Python Fundamentals")
    
    # Variable declarations and basic operations
    num1 = 10
    num2 = 5
    
    # Arithmetic operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2
    
    print(f"Addition: {num1} + {num2} = {addition}")
    print(f"Subtraction: {num1} - {num2} = {subtraction}")
    print(f"Multiplication: {num1} * {num2} = {multiplication}")
    print(f"Division: {num1} / {num2} = {division}")
    
    # String operations
    greeting = "Hello"
    name = "AI Student"
    message = f"{greeting}, {name}!"
    print(f"String concatenation: {message}")
    
    # List operations
    numbers = [1, 2, 3, 4, 5]
    print(f"List: {numbers}")
    print(f"List length: {len(numbers)}")
    print(f"First element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")
    
    # Conditional statements
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} is equal to {num2}")

if __name__ == "__main__":
    main()