# Lab 2 - Function Analysis + Lab 1 Pre-lab functions

# Function 1
def function1(number):
    total = 0
    for i in range(number):
        x = i + 1
        total += x * x
    return total

# Function 2
def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6

# Function 3
def function3(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp

# Function 4
def function4(number):
    total = 1
    for i in range(1, number):
        total *= i + 1
    return total

# Lab 1: Recursive Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Correct sum_to_goal from Lab 1 (2-sum product logic)
def sum_to_goal(numbers, goal):
    seen = set()
    for number in numbers:
        complement = goal - number
        if complement in seen:
            return number * complement
        seen.add(number)
    return 0
