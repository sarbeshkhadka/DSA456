# DSA456 - Lab 4

Group Members
Name: Adheesh Tiwari  
Email: atiwari28@myseneca.ca  
Student ID: 180324238  
Name: Sarbesh Khadka
Email: skhadka62@myseneca.ca
Student Id: 188383236

# Part A: Questions about the Video

# 1. What sorting algorithm was the speaker trying to improve?
The speaker, Andrei Alexandrescu, focused on improving introsort. This is a smart hybrid algorithm that starts with quicksort and switches to heapsort or insertion sort depending on how the data behaves, trying to get the best of all worlds.

# 2. At what partition size does Visual Studio (VS) perform a simpler sort algorithm instead of continuing to partition?
Visual Studio changes gears and switches to a simpler sorting method like insertion sort when the partition size drops to 32.

# 3. At what partition size does GNU perform a simpler sort algorithm instead of continuing to partition?
GNU kicks in the simpler insertion sort when the partition size hits 16.

# 4. Why doesn’t switching to a binary search in insertion sort improve performance?
Binary search sounds faster because it finds where to insert faster. But in real code, it doesn’t help much because the real cost is moving the items in the array, not finding the spot. Also, binary search introduces more branches, and CPUs don’t love that—it slows them down.

# 5. Describe what is meant by branch prediction.
Branch prediction is the CPU trying to guess what will happen in an ‘if’ statement before it actually knows. If it guesses wrong, it has to backtrack and redo some work, which wastes time. It’s like a waiter bringing you the wrong dish because they assumed what you’d order.

# 6. What is meant by informational entropy?
Entropy here just means how disordered the data is. If it's super mixed up, the algorithm has to do more work to sort it. If it's already almost sorted, it's a much easier job.

# 7. Explain unguarded_insertion_sort() and why it is faster.
Unguarded insertion sort skips some of the usual boundary checks. It’s like trusting that the lowest value is already at the front, so you don’t have to keep checking if you're at the beginning. By doing make_heap() first, you set up the data in a way that allows this trust, and it runs faster because it avoids constant checking.

# 8. What does incorporating conditionals into arithmetic mean? Provide an example.
Instead of using if-else, you use math tricks to make a decision. For example, using bitwise operations instead of writing `if (a < b)`. It avoids the if statement, and the CPU doesn’t have to guess which path you’ll take—so it runs smoother.

# 9. Describe the bug in GNU’s implementation.
There was a situation where the algorithm assumed things about the data that weren’t always true. This led to wrong sorting results in some edge cases. Basically, it trusted the data too much and didn’t check carefully enough.

# 10. What metric does the speaker think is missing in performance graphs?
He points out that while time and number of moves are tracked, they miss measuring how much 'order' is being restored—this is where entropy reduction comes in. It tells us how efficiently the algorithm is making progress.

# 11. What does the speaker mean by "fast code is left-leaning"?
This means code runs faster when the ‘if’ conditions tend to be true more often, because CPUs are usually better at guessing that branches will be taken.

# 12. What does the speaker mean by "not mixing hot and cold code"?
Hot code runs all the time. Cold code runs rarely. Mixing them is like putting snacks and winter coats in the same drawer—it makes things messy. Keeping hot and cold code separate helps the CPU run faster.


# Part B: Reflection (Individual)

# What did you/your team find most challenging to understand in the video?
The most difficult thing was understanding the extent to which performance is contingent upon such CPU characteristics as branch prediction. Sometimes we think of sorting as merely the rearrangement of data but the video made us realize that it is just as crucial to understand how code communicates with the CPU, which became clear to us overtime.
# What is the most surprising thing you learned?
The news that learning binary search does not actually speed up insertion sort by much in reality came as a surprise. I had always believed that a reduced number of comparisons would make it run quicker, though this revealed that such things as memory access pattern and CPU prediction have an even greater influence.


# Has the video given you ideas on how you can write better/faster code?
Absolutely. Now I know how crucial it is to create such code that is predictable to the CPU. In the future, I will give more consideration to the way I use branches and conditionals and my goal is to use code that is more friendly to the CPU not just working code

# References

- Alexandrescu, A. (2019). *Sorting Algorithms: Speed Is Found In The Minds of People*. [CppCon 2019](https://www.youtube.com/watch?v=FJJTYQYB1JQ)
- https://en.algorithmica.org/hpc/
- Knuth, D. E. (1998). *The Art of Computer Programming: Volume 3: Sorting and Searching*
