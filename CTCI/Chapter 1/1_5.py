# One Away: There are three types of edits that can be performed on strings: insert a character, remove a character,
#           or replace a character. Giver two strings, write a function to check if they are one edit (or zero edits) away.

# Use a hashtable for str1 and keep a count of replaces and additions. Only replaces and additions will cause similar behavior
# Run time: O(N + M)
# Space complexity: O(N)
def oneAway1(str1, str2):
    if str1 == str2:
        return True
    addAndReplace = 0
    str1Map = {}
    for c in str1:
        str1Map[c] = 0
    for c in str2:
        if c not in str1Map:
            addAndReplace += 1
    if len(str2) < len(str1Map):
        if addAndReplace < 1:
            return True
        else:
            return False
    if addAndReplace < 2:
        return True
    return False

# Use a ascii value array to map characters to count array


print(oneAway1("pale", "palee"))

