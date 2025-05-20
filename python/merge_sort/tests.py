import unittest
from merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([42]), [42])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(merge_sort([4, 2, 5, 2, 3, 4]), [2, 2, 3, 4, 4, 5])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-3, -1, -2, 0, 2, 1]), [-3, -2, -1, 0, 1, 2])

    def test_mixed_types(self):
        # This should raise a TypeError in Python 3 if types are not comparable
        with self.assertRaises(TypeError):
            merge_sort([1, "a", 3])

    def test_large_list(self):
        import random
        arr = random.sample(range(1000), 1000)
        self.assertEqual(merge_sort(arr), sorted(arr))

if __name__ == '__main__':
    unittest.main()
