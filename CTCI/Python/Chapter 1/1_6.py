# String Compression
# Run time: O(N)
# Space complexity: O(N)
import unittest

def stringCompression(s):
    compressed = ''
    charCount = 0
    i = 0
    j = 0
    while i < len(s):
        charCount = 0
        while j < len(s) and s[i] == s[j]:
            j+=1
            charCount += 1
        compressed += s[i] + str(charCount)
        i = j
    if len(compressed) > len(s):
        return s
    return compressed

class Test(unittest.TestCase):
    data = [
        ('aabbcc', 'a2b2c2'),
        ('a', 'a'),
        ('bb', 'b2'),
        ('', ''),
    ]

    def test_one_away(self):
        for [test_s1, expected] in self.data:
            actual1 = stringCompression(test_s1)
            self.assertEqual(actual1, expected)

if __name__ == "__main__":
    unittest.main()


