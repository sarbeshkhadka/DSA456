
# Lab 3: Recursive Functions - Analysis and Reflection

## Part A: Recursive Functions

### Function 1: Factorial Function

```python
def factorial(number):
    if number == 0:
        return 1
    return number * factorial(number - 1)
```

- **Purpose**: This function calculates the factorial of a number recursively. The base case is when the number is 0, which returns 1. Otherwise, it multiplies the number by the result of the factorial of the previous number.
- **Example**: `factorial(5)` returns `5 * 4 * 3 * 2 * 1 = 120`

### Function 2: Linear Search

```python
def linear_search(my_list, key, index=0):
    if index >= len(my_list):
        return -1
    if my_list[index] == key:
        return index
    return linear_search(my_list, key, index + 1)
```

- **Purpose**: This function searches for a key in a list recursively by checking one element at a time. If the element is found, it returns the index; otherwise, it returns -1.
- **Example**: `linear_search([1, 2, 3, 4], 3)` returns `2` (index of 3 in the list).

### Function 3: Binary Search

```python
def binary_search(sorted_list, key, low=0, high=None):
    if high is None:
        high = len(sorted_list) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if sorted_list[mid] == key:
        return mid
    elif sorted_list[mid] > key:
        return binary_search(sorted_list, key, low, mid - 1)
    else:
        return binary_search(sorted_list, key, mid + 1, high)
```

- **Purpose**: This function searches for a key in a sorted list using binary search recursively. It compares the key with the middle element and reduces the search range by half in each call.
- **Example**: `binary_search([1, 2, 3, 4, 5], 4)` returns `3` (index of 4 in the list).

## Part B: Analysis

### Function 1: Recursive Multiplication Function

```python
def function1(value, number):
    if number == 0:
        return 1
    elif number == 1:
        return value
    else:
        return value * function1(value, number - 1)
```

**Analysis**:
- This function recursively multiplies `value` by itself `number` times.
- **Time Complexity**: **O(n)**, where `n` is the `number`. The function makes `n` recursive calls.
- **Space Complexity**: **O(n)** due to the recursion depth.

### Function 2: Recursive Palindrome Check

```python
def recursive_function2(mystring, a, b):
    if a >= b:
        return True
    else:
        if mystring[a] != mystring[b]:
            return False
        else:
            return recursive_function2(mystring, a + 1, b - 1)
```

**Analysis**:
- This function checks if a string is a palindrome by comparing characters from both ends of the string.
- **Time Complexity**: **O(n)**, where `n` is the length of the string.
- **Space Complexity**: **O(n)**, due to recursive stack calls for each comparison.

### Function 3: Optimized Power Function (Optional)

```python
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
```

**Analysis**:
- This function calculates `value` raised to the power of `number` using an optimized divide-and-conquer approach.
- **Time Complexity**: **O(log n)**, which makes it more efficient than a direct multiplication approach.
- **Space Complexity**: **O(log n)**, due to the recursive calls.

## Part C: Reflection

### Approach to Writing Recursive Functions

1. **Base Case**: Every recursive function must have a base case to stop the recursion. This case should handle the simplest possible input or the end condition.
2. **Recursive Case**: After solving the base case, reduce the problem size by calling the function with smaller or simpler inputs.
3. **Termination**: Ensure that each recursive call makes progress towards the base case and will eventually terminate.

### Analyzing Recursive Functions

- **Time Complexity**: The time complexity is based on how many times the function calls itself and the number of operations performed in each call.
- **Space Complexity**: The space complexity depends on how deep the recursive calls go, which is related to the number of function calls that need to be stored in memory at once.

**Difference from Non-Recursive Functions**:
- Non-recursive functions generally loop through the data using iterations, which does not involve maintaining a call stack.
- Recursive functions, on the other hand, involve a call stack where each function call is stored and then returns a value. This can lead to greater space complexity, especially for deep recursions.

