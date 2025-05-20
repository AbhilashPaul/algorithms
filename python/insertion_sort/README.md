### Insertion Sort
Why Use Insertion Sort?
- Fast: for very small data sets (even faster than merge sort and quick sort, which we'll cover later)
- Adaptive: Faster for partially sorted data sets
- Stable: Does not change the relative order of elements with equal keys
- In-Place: Only requires a constant amount of memory
- Inline: Can sort a list as it receives it




Why Is Insertion Sort Fast for Small Lists?

Many production sorting implementations use insertion sort for very small inputs under a certain threshold (very small, like 10-ish), and switch to something like quicksort for larger inputs. They use insertion sort because:
- There is no recursion overhead
- It has a tiny memory footprint
- It's a stable sort as described above

Time complexity: O(N<sup>2</sup>)  
Space complexity: O(1)  
