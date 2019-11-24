# Triple Step

# Run time: O(3^N)
# Space Complexity: O(N)
def countHops1(n):
    if n < 0 :
        return 0
    elif n==0:
        return 1
    else:
        return countHops1(n-3) + countHops1(n-2) + countHops1(n-1)

# Run time: O(N)
# Space Complexity: O(N)
def countHops2(n):
    memo = [-1] * (n+1)
    return countHopsHelper(n, memo)

def countHopsHelper(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        if memo[n] != -1:
            return memo[n]
        else:
            memo[n] = countHopsHelper(n-1, memo) + countHopsHelper(n-2, memo) + countHopsHelper(n-3, memo)
    return memo[n]

print(countHops1(4))
print(countHops2(4))