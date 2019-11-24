# Return kth to the last: Implement an algorithm to find the kth to last element of a singly linked list
# Inputs: Singly ll, k
# Output: value of kth to last element

from LinkedList import LinkedList

# Find length of ll and then go to len - k element and return that
# Run time: O(N)
# Space Complexity: O(1)
def findK1(ll, k):
    if ll == None:
        return None
    # find length
    lenLL = 0
    ptr = ll.head
    while ptr:
        lenLL += 1
        ptr = ptr.next
    if k >= lenLL:
        return None
    count = 1
    ptr = ll.head
    while count != lenLL - k:
        ptr = ptr.next
        count += 1
    return ptr.value

# With a runner

def findK2(ll, k):
    if ll is None:
        return ll
    runner = ll.head
    runnerPosition = 0
    while runnerPosition != k and runner.next:
        runner = runner.next
        runnerPosition += 1
    ptr = ll.head
    while runner.next:
        ptr = ptr.next
        runner = runner.next
    return ptr.value



ll = LinkedList()
ll.generate(10, 0, 9)
print(ll)
print(findK2(ll, 10))
