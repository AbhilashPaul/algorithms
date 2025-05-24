import unittest
from quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(quick_sort([], 0, 0), [])

    def test_single_element(self):
        self.assertEqual(quick_sort([42], 0, 0), [42])

    def test_sorted_list(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5], 0, 4), [1, 2, 3, 4, 5])

    def test_reverse_list(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1], 0, 4), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(quick_sort([4, 2, 5, 2, 3, 4], 0, 5), [2, 2, 3, 4, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(quick_sort([-3, -1, -2, 0, 2, 1], 0, 5), [-3, -2, -1, 0, 1, 2])

    def test_mixed_types(self):
        # This should raise a TypeError in Python 3 if types are not comparable
        with self.assertRaises(TypeError):
            quick_sort([1, "a", 3], 0, 2)

    def test_large_list(self):
        import random
        arr = random.sample(range(1000), 1000)
        self.assertEqual(quick_sort(arr, 0, 999), sorted(arr))

if __name__ == '__main__':
    unittest.main()
