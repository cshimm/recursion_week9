import unittest

def reverse_string(string):
    arr = list(string)
    helper(0, len(arr) - 1, arr)
    reversed = ''.join(arr)
    return reversed

def helper(l, r, arr):
    if l >= r: return
    arr[l], arr[r] = arr[r], arr[l]
    return helper(l + 1, r - 1, arr)

class TestReverse_String(unittest.TestCase):
    def test_reverse_string(self):
        test_string = 'ABCDE'
        result = reverse_string(test_string)
        self.assertEqual(result, 'EDCBA')

    def test_empty(self):
        test_string = ''
        result = reverse_string(test_string)
        self.assertEqual(result, '')

    def test_single_character(self):
        test_string = 'A'
        result = reverse_string(test_string)
        self.assertEqual(result, 'A')

    def test_two_characters(self):
        test_string = 'AB'
        result = reverse_string(test_string)
        self.assertEqual(result, 'BA')
    
    def test_really_long_string(self):
        long_string = ''.join([str(i) for i in range(100)])
        result = reverse_string(long_string)
        self.assertEqual(result, ''.join(reversed(long_string)))

    def test_palindrome(self):
        palindrome = 'racecar'
        result = reverse_string(palindrome)
        self.assertEqual(result, palindrome)

if '__main__' == __name__:
    unittest.main()