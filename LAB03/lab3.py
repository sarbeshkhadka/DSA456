# Recursive Function 1: Factorial Calculation
def factorial(number):
    # Base case: factorial of 0 is 1
    if number == 0:
        return 1
    # Recursive case: number * factorial(number - 1)
    return number * factorial(number - 1)

# Recursive Function 2: Linear Search
def linear_search(my_list, key, index=0):
    # Base case: if index exceeds list length, key is not found
    if index >= len(my_list):
        return -1
    # If the key is found at the current index
    if my_list[index] == key:
        return index
    # Recursive case: search further in the list
    return linear_search(my_list, key, index + 1)

# Recursive Function 3: Binary Search
def binary_search(sorted_list, key, low=0, high=None):
    if high is None:
        high = len(sorted_list) - 1  # Set high to last index if not provided
    
    # Base case: key is not found
    if low > high:
        return -1
    
    mid = (low + high) // 2
    # If key is found at mid
    if sorted_list[mid] == key:
        return mid
    # Recursive case: search in the left or right half
    elif sorted_list[mid] > key:
        return binary_search(sorted_list, key, low, mid - 1)
    else:
        return binary_search(sorted_list, key, mid + 1, high)

# Helper Function 1: Function1 - Recursive Multiplication
def function1(value, number):
    if number == 0:
        return 1
    elif number == 1:
        return value
    else:
        return value * function1(value, number - 1)

# Helper Function 2: Recursive Palindrome Check
def recursive_function2(mystring, a, b):
    if a >= b:
        return True
    else:
        if mystring[a] != mystring[b]:
            return False
        else:
            return recursive_function2(mystring, a + 1, b - 1)

# Wrapper Function 2: Function2 - Palindrome Check
def function2(mystring):
    return recursive_function2(mystring, 0, len(mystring) - 1)

# Optional Function 3: Optimized Power Function
def function3(value, number):
    if number == 0:
        return 1
    elif number == 1:
        return value
    else:
        half = number // 2
        result = function3(value, half)
        if number % 2 == 0:
            return result * result
        else:
            return value * result * result
