# Palindrome permutation: Given a string, write a function to check if it is a permutation of a palindrome.
#                         A palindrome is a word or phrase that is the same forwards and backwards. A 
#                         permutation is a rearrangement of letters. A permutation does not need to be limited
#                         to just dictionary words.
# Assumtions: permuations will not be case sensitive. Convert all input to lower case
#             white spaces matter>]. So "abcd" and " abcd" are not permutations of each other

import unittest
# Notice that a palindrome will always have every except one character appearing twice. Or it will have every character
# appearing twice. No more than one character is odd. 
# Run time: O(N)
# Space complexity: O(128) = O(1)
def palindromePermutation(str):
    char_Set = [0] * 128
    numberOfOddChars = 0
    for c in str:
        value = ord(c)
        char_Set[value] += 1
        if char_Set[value] % 2 != 0:
            numberOfOddChars += 1
        else:
            numberOfOddChars -=1
    if numberOfOddChars > 1:
        return False
    return True

class Test(unittest.TestCase):
    dataTrue = (('malayalam'), ('a'), (' '), ('abab'))
    dataFalse = (('aabc'), ('cd'), ('cat'), ('ugly'))

    def test_unique(self):
        for test in self.dataTrue:
            actual1 = palindromePermutation(test)
            self.assertTrue(actual1)
        for test in self.dataFalse:
            actual1 = palindromePermutation(test)
            self.assertFalse(actual1)

if __name__ == "__main__":
    unittest.main()


    