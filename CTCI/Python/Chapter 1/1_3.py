# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient 
#         space at the end to hold the additional characters, and that you are given the "true" length of the string.
#         IDEA: Use the same string with no extra space --> Space Complexity = O(1)

# Count number of spaces. Each space need 3 'slots' in return array. So shift the rest by 3. Str is a char array
# Run time: O(N)
# Space complexity: O(1)
def URLify1(str, trueLength):
    numOfSpaces = 0

print(URLify1(" ", 13))        
            
