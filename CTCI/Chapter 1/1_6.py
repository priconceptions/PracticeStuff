# String Compression
# Run time: O(N)
# Space complexity: O(N)
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

print(stringCompression("abbbccccddddddd"))


