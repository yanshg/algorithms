#!/usr/bin/python
"""Unit tests for binary_search.py"""

import unittest
from binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    
    def test_found_at_beginning(self):
        """Test searching for element at the beginning"""
        nums = [1, 4, 7, 9, 12, 15, 23, 45, 56, 78]
        result = binary_search(nums, 1)
        self.assertEqual(result, 0)
    
    def test_found_at_end(self):
        """Test searching for element at the end"""
        nums = [1, 4, 7, 9, 12, 15, 23, 45, 56, 78]
        result = binary_search(nums, 78)
        self.assertEqual(result, 9)
    
    def test_found_at_middle(self):
        """Test searching for element in the middle"""
        nums = [1, 4, 7, 9, 12, 15, 23, 45, 56, 78]
        result = binary_search(nums, 12)
        self.assertEqual(result, 4)
    
    def test_not_found(self):
        """Test searching for element that doesn't exist"""
        nums = [1, 4, 7, 9, 12, 15, 23, 45, 56, 78]
        result = binary_search(nums, 100)
        self.assertEqual(result, -1)
    
    def test_not_found_smaller_than_min(self):
        """Test searching for element smaller than minimum"""
        nums = [1, 4, 7, 9, 12, 15, 23, 45, 56, 78]
        result = binary_search(nums, 0)
        self.assertEqual(result, -1)
    
    def test_single_element_found(self):
        """Test searching in single element array"""
        nums = [5]
        result = binary_search(nums, 5)
        self.assertEqual(result, 0)
    
    def test_single_element_not_found(self):
        """Test searching for non-existent element in single element array"""
        nums = [5]
        result = binary_search(nums, 3)
        self.assertEqual(result, -1)
    
    def test_empty_array(self):
        """Test searching in empty array"""
        nums = []
        result = binary_search(nums, 5)
        self.assertEqual(result, -1)
    
    def test_duplicate_elements(self):
        """Test searching with duplicate elements (should find one occurrence)"""
        nums = [1, 2, 2, 2, 3, 4, 5]
        result = binary_search(nums, 2)
        # Should find one of the occurrences (implementation dependent)
        self.assertIn(result, [1, 2, 3])
    
    def test_large_array(self):
        """Test searching in large array"""
        nums = list(range(1000))
        result = binary_search(nums, 500)
        self.assertEqual(result, 500)
        result = binary_search(nums, 999)
        self.assertEqual(result, 999)
        result = binary_search(nums, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()

