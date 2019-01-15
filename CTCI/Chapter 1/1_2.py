# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
# Assumptions: Case sensitive. So permutation("abcd", "Abcd") is False
#              white spaces matter. So permutation(" abcd", "abcd") is False

import unittest

# Sort and compare
# Run time: O(NlogN) + O(N)  = O(NlogN)
# Space complexity: O(N)
def permutation1(str1, str2):
    if len(str1) != len(str2):
        return False
    l1 = sorted(str1)
    l2 = sorted(str2)
    if l1 == l2:
        return True
    return False

# Use hash tables for both strings
# Run time: O(N)
# Space complexity: O(N)
def permutation2(str1, str2):
    if len(str1) != len(str2):
        return False
    hashStr1 = {}
    hashStr2 = {}
    for c1 in str1:
        hashStr1[c1] = 0
    for c2 in str2:
        hashStr2[c2] = 0
    for c in str2:
        if c not in hashStr1:
            return False
    for c in str1:
        if c not in hashStr2:
            return False
    return True

# Permutation of two strings means that the two strings have the same character counts
# Run time: O(N)
# Space complexity: O(128) or O(1)
def permutation3(str1, str2):
    if len(str1) != len(str2):
        return False
    charCounts = [0] * 128
    for c in str1:
        value = ord(c)
        charCounts[value] += 1
    for c in str2:
        value = ord(c)
        charCounts[value] -= 1
        if charCounts[value] < 0:
            return False
    return True
    

class Test(unittest.TestCase):
    dataTrue = (('abcd', 'bcda'), ('cd', 'dc'), ('', ''), ('  ', '  '))
    dataFalse = (('aabc', 'abcd'), ('cc', 'dc'), ('  ', '   '), ('4', '5'))

    def test_unique(self):
        for test in self.dataTrue:
            actual1 = permutation1(*test)
            actual2 = permutation2(*test)
            actual3 = permutation3(*test)
            self.assertTrue(actual1)
            self.assertTrue(actual2)
            self.assertTrue(actual3)
        for test in self.dataFalse:
            actual1 = permutation1(*test)
            actual2 = permutation2(*test)
            actual3 = permutation3(*test)
            self.assertFalse(actual1)
            self.assertFalse(actual2)
            self.assertFalse(actual3)

if __name__ == "__main__":
    unittest.main()
