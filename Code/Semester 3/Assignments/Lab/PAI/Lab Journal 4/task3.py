# Lab Journal 4 - Task 3: Control Flow and Functions
# Programming for Artificial Intelligence

def fibonacci(n):
    """Generate Fibonacci sequence up to n terms"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence

def is_prime(num):
    """Check if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    print("Lab Journal 4 - Task 3: Control Flow and Functions")
    
    # Fibonacci sequence
    n_terms = 10
    fib_seq = fibonacci(n_terms)
    print(f"Fibonacci sequence ({n_terms} terms): {fib_seq}")
    
    # Prime number checking
    numbers_to_check = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    prime_numbers = []
    
    for num in numbers_to_check:
        if is_prime(num):
            prime_numbers.append(num)
    
    print(f"Prime numbers from {numbers_to_check}: {prime_numbers}")
    
    # Loop examples
    print("Even numbers from 1 to 20:")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i, end=" ")
    print()

if __name__ == "__main__":
    main()