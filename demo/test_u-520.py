import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from u_520 import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome('madam'))
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('python'))

    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome('MadAm'))
        self.assertTrue(is_palindrome('RaceCar'))

    def test_with_spaces(self):
        self.assertTrue(is_palindrome('nurses run'))
        self.assertTrue(is_palindrome('A man a plan a canal Panama'))
        self.assertFalse(is_palindrome('open ai'))

if __name__ == '__main__':
    unittest.main()
