import unittest
from insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

    def test_single_element(self):
        self.assertEqual(insertion_sort([42]), [42])

    def test_sorted_list(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(insertion_sort([3, 1, 4, 2, 5]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(insertion_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

    def test_negative_numbers(self):
        self.assertEqual(insertion_sort([0, -1, 5, -3, 2]), [-3, -1, 0, 2, 5])

    def test_all_equal(self):
        self.assertEqual(insertion_sort([7, 7, 7, 7]), [7, 7, 7, 7])

if __name__ == '__main__':
    unittest.main()
