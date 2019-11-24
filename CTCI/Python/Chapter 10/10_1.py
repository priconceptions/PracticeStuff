
# Run time: O(N) N is the length of B
# Space Complexity: O(1) -- no auxiliary space needed
def sortedMerge(A, B, lastA, lastB):
    indexA = lastA - 1
    indexB = lastB - 1
    indexMerged = indexA + indexB + 1
    while indexB >= 0:
        if indexA >= 0 and A[indexA] > B[indexB]:
            A[indexMerged] = A[indexA]
            indexA -= 1
        else:
            A[indexMerged] = B[indexB]
            indexB -= 1
        indexMerged -= 1

A = [1,9,11,12, None, None, None, None]
B = [2,7,10,13]
lastA = 4
lastB = 4
sortedMerge(A,B, lastA, lastB)
print(A)
