### Merge sort

Good choice when you need a fast sorting algorithm and memory is not an issue.

Pros:

- Fast: Merge sort is much faster than bubble sort. O(n*log(n)) instead of O(n^2).
- Stable: Merge sort is a stable sort which means that values with duplicate keys in the original list will be in the same order in the sorted list.

Cons:

- Memory usage: Most sorting algorithms can be performed using a single copy of the original array. Merge sort requires extra subarrays in memory.
- Recursive: Merge sort requires many recursive function calls, and in many languages (like Python), this can incur a performance penalty.

Time complexity: O(NlogN)  
Space complexity: O(n)  
