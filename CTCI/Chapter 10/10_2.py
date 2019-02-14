# Run time:
#            go through each word in the array of words and sort them
#                   length of word = k -- sorting each becomes O(klogk)
#                   number of words in array = n
#                   Total = O(n*klogk)
#            go through eachkey and put it in array -- O(N)
#     TOTAL = O(n*klogk)
# Space Complexity: 

def groupAnagrams(S):
    anagramDict = {}
    for word in S:
        charArr = list(word)
        charArr.sort()
        newWord = ''.join(charArr)
        if newWord in anagramDict:
            anagramDict[newWord].append(word)
        elif newWord not in anagramDict:
            anagramDict[newWord] = [word]
    
    i = 0
    for key in anagramDict:
        for word in anagramDict[key]:
            S[i] = word
            i += 1

    return S

S = ['ant', 'cinema', 'nat', 'iceman', 'mat', 'iecman', 'tam']
print(groupAnagrams(S))