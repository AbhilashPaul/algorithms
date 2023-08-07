import unittest
from linear_search import linear_search 

class TestLinearSearch(unittest.TestCase):
    def test_linear_search_value_not_found_in_given_array(self):
        array = [9, 5, 2, 6, 4 , 8, 3, 4]
        self.assertIsNone(linear_search(array, 1))
        
    def test_linear_search_value_found_in_given_array(self):
        unordered_array = [2, 3, 5, 6, 7 , 8, 10, 12]
        assert (linear_search(unordered_array, 10)) == 6


if __name__ == '__main__':
    unittest.main()