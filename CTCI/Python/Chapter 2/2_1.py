# Remove Dups: Write code to remove duplicates from an unsorted linked list.

from LinkedList import LinkedList

# With a hashset
# Run time: O(N)
# Space Complexity: O(N) in the worst case when no duplicates exist
def removeDups1(ll):
    if ll is None or ll.head.next is None:
        return ll
    llSet = []
    prev = ll.head
    ptr = ll.head.next
    llSet.append(ll.head.value)
    while ptr:
        if ptr.value in llSet:
            prev.next = ptr.next
            ptr =  prev.next
        else:
            llSet.append(ptr.value)
            ptr = ptr.next
            prev = prev.next

# Without a temporary buffer
# Run time: O(N^2)
# Space Complexity: O(1)
def removeDups2(ll):
    if ll.head == None or ll.head.next == None:
        return ll
    ptr = ll.head
    while ptr:
        prev = ptr
        ptrRunner = ptr.next
        while ptrRunner:
            if ptrRunner.value == ptr.value:
                prev.next = ptrRunner.next
                ptrRunner.next = None
                ptrRunner = prev.next
            else:
                ptrRunner = ptrRunner.next
                prev = prev.next
        ptr = ptr.next



ll = LinkedList()
ll.generate(10, 0, 9)
print(ll)
removeDups1(ll)
print(ll)


ll.generate(10, 0, 9)
print(ll)
removeDups2(ll)
print(ll)
