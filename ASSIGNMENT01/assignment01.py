import random
import time
import sys
import matplotlib.pyplot as plt

# Set a higher recursion limit for quick sort on large lists.
sys.setrecursionlimit(20000)

# --- Step 1 & 2: Sorting Functions with T(n) Calculation ---

def bubble_sort(my_list):
    """Sorts a list using Bubble Sort and returns the operation count."""
    steps = 0
    n = len(my_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            steps += 1  # For the comparison
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                steps += 3  # 3 operations for a swap
    return steps

def selection_sort(my_list):
    """Sorts a list using Selection Sort and returns the operation count."""
    steps = 0
    n = len(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps += 1  # For the comparison
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
        steps += 3  # 3 operations for the swap
    return steps

def insertion_sort(my_list):
    """Sorts a list using Insertion Sort and returns the operation count."""
    steps = 0
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        steps += 2  # For the key assignment and initialization of j
        
        comparison_steps = 0
        while j >= 0 and key < my_list[j]:
            comparison_steps += 1 # Each check in the while loop is a comparison
            my_list[j + 1] = my_list[j]
            j -= 1
            steps += 2  # 1 for the assignment, 1 for decrementing j
        
        # Add the cost of comparisons. There's always one last comparison that fails.
        steps += comparison_steps + 1

        my_list[j + 1] = key
        steps += 1  # For placing the key in its sorted position
    return steps

def merge_sort(my_list):
    """Sorts a list using Merge Sort and returns the operation count."""
    steps = 0
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        steps += len(my_list) # Cost of splitting the list

        steps += merge_sort(left_half)
        steps += merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            steps += 1 # Comparison
            if left_half[i] < right_half[j]:
                my_list[k] = left_half[i]
                i += 1
            else:
                my_list[k] = right_half[j]
                j += 1
            k += 1
            steps += 1 # Assignment to my_list[k]

        while i < len(left_half):
            my_list[k] = left_half[i]
            i += 1
            k += 1
            steps += 1 # Assignment
        
        while j < len(right_half):
            my_list[k] = right_half[j]
            j += 1
            k += 1
            steps += 1 # Assignment
    return steps

def _partition(my_list, low, high):
    """Helper for quick_sort, partitions list and counts steps."""
    steps = 0
    pivot = my_list[high]
    i = low - 1
    steps += 2 # 2 assignments

    for j in range(low, high):
        steps += 1 # Comparison
        if my_list[j] <= pivot:
            i += 1
            my_list[i], my_list[j] = my_list[j], my_list[i]
            steps += 4 # 1 assignment for i, 3 for swap
            
    my_list[i + 1], my_list[high] = my_list[high], my_list[i + 1]
    steps += 3 # Swap
    
    return i + 1, steps

def _quick_sort_helper(my_list, low, high):
    """Recursive helper for quick_sort that returns step count."""
    steps = 0
    if low < high:
        pi, partition_steps = _partition(my_list, low, high)
        steps += partition_steps

        steps += _quick_sort_helper(my_list, low, pi - 1)
        steps += _quick_sort_helper(my_list, pi + 1, high)
    return steps

def quick_sort(my_list):
    """Sorts a list using Quick Sort and returns operation count."""
    return _quick_sort_helper(my_list, 0, len(my_list) - 1)

# --- Main execution and analysis ---

def step1_initial_test():
    """Step 1: Verify that the sorting functions work correctly."""
    print("--- Step 1: Sorting Functionality Check ---")
    list_size = 100
    original_list = [random.randint(0, 1000) for _ in range(list_size)]
    print(f"Generated a random list of {list_size} elements to test sorting.")
    
    sorted_verification_list = sorted(original_list)

    sort_functions = {
        "Bubble Sort": bubble_sort, "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort, "Merge Sort": merge_sort, "Quick Sort": quick_sort
    }

    all_passed = True
    for name, func in sort_functions.items():
        list_to_sort = original_list.copy()
        func(list_to_sort) # We ignore the returned steps for this test
        if list_to_sort == sorted_verification_list:
            print(f"✅ {name}: Successfully sorted.")
        else:
            print(f"❌ {name}: Failed to sort correctly.")
            all_passed = False
    
    if not all_passed:
        print("\nWarning: Some sorting functions have issues.")
    print("-" * 50)


def step2_tn_analysis():
    """Step 2: Analyze T(n) for best, average, and worst cases."""
    print("\n--- Step 2: T(n) Analysis ---")
    
    list_size = 20
    avg_case_list = [random.randint(0, 100) for _ in range(list_size)]
    best_case_list = sorted(avg_case_list)
    worst_case_list = sorted(avg_case_list, reverse=True)

    print(f"Testing with a list of size {list_size} for Best, Average, and Worst Cases.")
    print("\nBest case: An already sorted list.")
    print("Worst case: A reverse-sorted list (for most algorithms here).")
    print("Average case: A randomly shuffled list.")

    sort_functions = {
        "Bubble Sort": bubble_sort, "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort, "Merge Sort": merge_sort, "Quick Sort": quick_sort
    }

    for name, func in sort_functions.items():
        print(f"\n--- {name} ---")
        # Note: Quicksort's worst case is a sorted list with our pivot choice.
        # Its best case is more complex, but a random list is a good proxy for average.
        best = best_case_list.copy()
        avg = avg_case_list.copy()
        worst = worst_case_list.copy()
        
        if name == "Quick Sort":
            # For our pivot implementation, sorted is worst, reverse-sorted is also worst.
             worst = best_case_list.copy()

        print(f"Best Case T(n):    {func(best)}")
        print(f"Average Case T(n): {func(avg)}")
        print(f"Worst Case T(n):   {func(worst)}")
    print("-" * 50)


def step3_and_4_plotting():
    """Steps 3 & 4: Plot T(n) and Execution Time vs. n for the worst-case scenario."""
    print("\n--- Step 3 & 4: Plotting T(n) and Execution Time vs. Input Size (n) ---")
    
    # Note: O(n^2) algorithms are very slow. We use smaller sizes for them.
    quadratic_sizes = [10, 50, 100, 250, 500, 1000, 2500]
    n_log_n_sizes = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

    sort_functions = {
        "Bubble Sort": (bubble_sort, quadratic_sizes),
        "Selection Sort": (selection_sort, quadratic_sizes),
        "Insertion Sort": (insertion_sort, quadratic_sizes),
        "Quick Sort": (quick_sort, quadratic_sizes), # Worst case is O(n^2)
        "Merge Sort": (merge_sort, n_log_n_sizes),
    }

    results_tn = {name: [] for name in sort_functions}
    results_time = {name: [] for name in sort_functions}
    actual_sizes = {name: sizes for name, (_, sizes) in sort_functions.items()}

    for name, (func, sizes) in sort_functions.items():
        print(f"Processing {name} for various list sizes...")
        for size in sizes:
            # Worst-case scenario: reversely sorted list
            # For our Quick Sort, a sorted list is the worst case.
            if name == "Quick Sort":
                worst_case_list = list(range(size))
            else:
                worst_case_list = list(range(size, 0, -1))
            
            # --- T(n) calculation ---
            l_copy_tn = worst_case_list.copy()
            steps = func(l_copy_tn)
            results_tn[name].append(steps)
            
            # --- Time measurement ---
            l_copy_time = worst_case_list.copy()
            start_time = time.perf_counter()
            func(l_copy_time)
            end_time = time.perf_counter()
            results_time[name].append(end_time - start_time)

    # --- Plotting ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 16))

    # Plot 1: T(n) vs n
    for name, data in results_tn.items():
        ax1.plot(actual_sizes[name], data, marker='o', linestyle='-', label=name)
    ax1.set_title('Step 3: Operation Count T(n) vs. List Size n (Worst Case)')
    ax1.set_xlabel('List Size (n)')
    ax1.set_ylabel('Number of Operations T(n)')
    ax1.legend()
    ax1.grid(True)
    ax1.set_xscale('log')
    ax1.set_yscale('log')

    # Plot 2: Time vs n
    for name, data in results_time.items():
        ax2.plot(actual_sizes[name], data, marker='o', linestyle='-', label=name)
    ax2.set_title('Step 4: Execution Time vs. List Size n (Worst Case)')
    ax2.set_xlabel('List Size (n)')
    ax2.set_ylabel('Time (seconds)')
    ax2.legend()
    ax2.grid(True)
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    
    plt.tight_layout()
    
    # Save the combined plot
    plt.savefig('sorting_analysis_plots.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("\n--- Interpretation of Results ---")
    print("Step 3 Plot (T(n) vs n):")
    print("- This plot shows the theoretical number of operations.")
    print("- On a log-log scale, an O(n^2) algorithm (Bubble, Selection, Insertion, worst-case Quick Sort) appears as a straight line with a slope of roughly 2.")
    print("- An O(n log n) algorithm (Merge Sort) appears as a line that is less steep than the O(n^2) algorithms.")
    print("- You should see the lines for the O(n^2) algorithms are parallel and steeper than the line for Merge Sort.")
    
    print("\nStep 4 Plot (Time vs n):")
    print("- This plot shows the actual wall-clock time taken.")
    print("- The shapes of the curves should be very similar to the T(n) plot. This confirms that the theoretical complexity (Big O) is a good predictor of real-world performance.")
    print("- You might notice some differences due to factors like memory access patterns, caching, and the specific implementation details of the Python interpreter, but the overall trend will hold.")
    print("- Merge Sort is clearly the most efficient for large lists, which is consistent with its O(n log n) complexity.")
    
    print(f"\nPlots have been saved as 'sorting_analysis_plots.png' in the current directory.")


if __name__ == "__main__":
    step1_initial_test()
    step2_tn_analysis()
    step3_and_4_plotting() 