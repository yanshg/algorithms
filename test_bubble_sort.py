#!/usr/bin/python
"""Unit tests for bubble_sort.py"""

import unittest
from bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    
    def test_basic_sort(self):
        """Test basic sorting functionality"""
        numbers = [13, 6, 23, 67, 45, 92, 4, 53, 25, 7]
        expected = sorted(numbers)
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)
    
    def test_already_sorted(self):
        """Test sorting an already sorted array"""
        numbers = [10, 20, 23, 67, 70, 92, 101, 153, 167, 700]
        expected = numbers[:]
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array"""
        numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = sorted(numbers)
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)
    
    def test_single_element(self):
        """Test sorting single element array"""
        numbers = [5]
        expected = [5]
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)
    
    def test_empty_array(self):
        """Test sorting empty array"""
        numbers = []
        expected = []
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)
    
    def test_duplicate_elements(self):
        """Test sorting array with duplicate elements"""
        numbers = [5, 2, 8, 2, 9, 1, 5, 5]
        expected = sorted(numbers)
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test sorting array with negative numbers"""
        numbers = [-5, -2, -8, 3, 1, -1, 0]
        expected = sorted(numbers)
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)
    
    def test_all_same_elements(self):
        """Test sorting array with all same elements"""
        numbers = [5, 5, 5, 5, 5]
        expected = [5, 5, 5, 5, 5]
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)
    
    def test_two_elements(self):
        """Test sorting array with two elements"""
        numbers = [2, 1]
        expected = [1, 2]
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)
    
    def test_large_array(self):
        """Test sorting large array"""
        numbers = list(range(100, 0, -1))
        expected = sorted(numbers)
        result = bubble_sort(numbers)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

