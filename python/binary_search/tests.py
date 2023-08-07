import unittest
from binary_search import binary_search 

class TestBinarySearch(unittest.TestCase):
    def test_unordered_array(self):
        unordered_array = [9, 5, 2, 6, 4 , 8, 3, 4]
        self.assertIsNone(binary_search(unordered_array, 3))
        
    def test_ordered_array(self):
        unordered_array = [2, 3, 5, 6, 7 , 8, 10, 12]
        assert (binary_search(unordered_array, 3)) == 1


if __name__ == '__main__':
    unittest.main()