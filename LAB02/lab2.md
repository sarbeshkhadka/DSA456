# Lab 2 - Function Analysis & Group Timing Comparison

## Part A: Function Analysis

### Function 1: `function1(number)`
```python
def function1(number):
    total = 0
    for i in range(number):
        x = i + 1
        total += x * x
    return total
```
- **Time Complexity**: O(n) 
- **Space Complexity**: O(1) 

### Function 2: `function2(number)`
```python
def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6
```
- **Time Complexity**: O(1) 
- **Space Complexity**: O(1) 

### Function 3: `function3(lst)`
```python
def function3(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                tmp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = tmp
```
- **Time Complexity**: O(n^2) 
- **Space Complexity**: O(1) 

### Function 4: `function4(number)`
```python
def function4(number):
    total = 1
    for i in range(1, number):
        total *= i + 1
    return total
```
- **Time Complexity**: O(n) 
- **Space Complexity**: O(1) 

---

## Part B & C: In-Lab Group Work

### Group Members
- Sarbesh Khadka (Solo)

### Timing Data
| Team member       | Timing for fibonacci | Timing for sum_to_goal |
|------------------|----------------------|--------------------------|
| Sarbesh Khadka   | 5.659                | 0.003                   |

### Performance Comparison Table
| Function         | Fastest | Slowest | Difference |
|------------------|---------|---------|------------|
| sum_to_goal      | 0.003   | 0.003   | 0.000      |
| fibonacci        | 5.659   | 5.659   | 0.000      |

### Summary
- As the only participant, Sarbesh Khadka’s results were consistent and served as a benchmark.
- Recursive `fibonacci` is known to be slower due to redundant calculations, whereas `sum_to_goal` is optimized and runs in linear time.

---

## Reflection
- Recursive functions like `fibonacci` have exponential time complexity and should be optimized using memoization or converted to iterative versions.
- Loop-based summations like `sum_to_goal` are efficient and scalable.
- Even solo testing can reveal major performance contrasts between recursive and iterative designs.

### Conclusion
- This lab reinforced the importance of algorithm choice and complexity awareness.
- Writing efficient code from the start saves time and resources during execution.
