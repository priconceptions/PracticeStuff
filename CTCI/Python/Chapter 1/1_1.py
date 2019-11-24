# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

import unittest
# Uses a hash table -- dict
# Average run time: O(N)
# Worst Case run time: O(N^2) 
# Space complexity: O(N)
def isUnique_1(str):
    strMap = {}
    for c in str:
        if c in strMap:
            return False
        else:
            strMap[c] = 0
    return True

# Uses the fact that ascii is 128 characters
# Run time: O(N) or could say O(1) b/c we know that the length of str is less that 128. So the loop will only run < 128 times
# Space complexity: O(128) or O(1)
def isUnique_2(str):
    if len(str) > 128:
        return False
    char_Set = [False] * 128
    for c in str:
        value = ord(c)
        if char_Set[value]:
            return False
        char_Set[value] = True
    return True

# Run time: O(N^2)
# Space complexity: O(1)
def isUnique_3(str):
    for i in range(0, len(str)):
        for j in range(0, len(str)):
            if i != j:
                if str[i] == str[j]:
                    return False
    return True

class Test(unittest.TestCase):
    dataTrue = [('abcd'), ('c'), (''), ('45fgh')]
    dataFalse = [('aabc'), ('cc'), ('  '), ('445ggh')]

    def test_unique(self):
        for test in self.dataTrue:
            actual1 = isUnique_1(test)
            actual2 = isUnique_2(test)
            actual3 = isUnique_3(test)
            self.assertTrue(actual1)
            self.assertTrue(actual2)
            self.assertTrue(actual3)
        for test in self.dataFalse:
            actual1 = isUnique_1(test)
            actual2 = isUnique_2(test)
            actual3 = isUnique_3(test)
            self.assertFalse(actual1)
            self.assertFalse(actual2)
            self.assertFalse(actual3)

if __name__ == "__main__":
    unittest.main()

