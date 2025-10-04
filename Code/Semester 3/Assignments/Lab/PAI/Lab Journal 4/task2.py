# Lab Journal 4 - Task 2: Data Structures and Operations
# Programming for Artificial Intelligence

def main():
    print("Lab Journal 4 - Task 2: Data Structures and Operations")
    
    # Lists
    fruits = ["apple", "banana", "orange", "grape"]
    print(f"Original list: {fruits}")
    
    fruits.append("mango")
    print(f"After append: {fruits}")
    
    fruits.remove("banana")
    print(f"After remove: {fruits}")
    
    # Dictionaries
    student = {
        "name": "John Doe",
        "age": 20,
        "course": "Programming for AI",
        "grade": "A"
    }
    
    print(f"Student info: {student}")
    print(f"Student name: {student['name']}")
    
    # Tuples
    coordinates = (10, 20)
    print(f"Coordinates: {coordinates}")
    
    # Sets
    unique_numbers = {1, 2, 3, 4, 5, 3, 2, 1}
    print(f"Unique numbers: {unique_numbers}")

if __name__ == "__main__":
    main()