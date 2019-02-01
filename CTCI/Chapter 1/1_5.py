# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character,
#           or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.


import unittest
# Use a hashtable for str1 and keep a count of replaces and additions. Only replaces and additions will cause similar behavior
# Run time: O(N + M)
# Space complexity: O(N)
def oneAway1(str1, str2):
    if str1 == str2:
        return True
    if abs(len(str1) - len(str2)) > 1:
        return False
    addAndReplace = 0
    str1Map = {}
    for c in str1:
        str1Map[c] = 0
    for c in str2:
        if c not in str1Map:
            if addAndReplace > 1:
                return False
            addAndReplace += 1
    if len(str2) < len(str1Map):
        if addAndReplace < 1:
            return True
        else:
            return False
    if addAndReplace < 2:
        return True
    return False

# Think about defninitions and get runtime to O(N)
# Replace --> str1 and str2 have the same length but different characters
# Insert --> len(str1) + 1 = len(str2) and all other characters are the same
# Remove --> len(str1) = len(str2) + 1 and all other characters are the same ; else false
# Run time: O(N) 
# Space complexity: O(1)
def oneAway2(str1, str2):
    if len(str1) == len(str2):
        return oneAwayReplace(str1, str2)
    elif len(str1) + 1 == len(str2):
        return oneAwayInsert(str1, str2)
    elif len(str1) == len(str2) + 1:
        return oneAwayInsert(str2, str1)
    return False

def oneAwayReplace(str1, str2):
    alreadyDifferent = False
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            if alreadyDifferent:
                return False
            alreadyDifferent = True
    return True

def oneAwayInsert(s1, s2):
    i1 = 0
    i2 = 0
    alreadyDifferent = False
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] != s2[i2]:
            if alreadyDifferent:
                return False
            alreadyDifferent = True
            i2 += 1
        else:
            i1 += 1
            i2 += 1
    return True

class Test(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual1 = oneAway1(test_s1, test_s2)
            actual2 = oneAway2(test_s1, test_s2)
            self.assertEqual(actual1, expected)
            self.assertEqual(actual2, expected)

if __name__ == "__main__":
    unittest.main()

