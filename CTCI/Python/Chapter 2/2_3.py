# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node).
# of a singly linked list, gievn only access to that node.

from LinkedList import LinkedList

def removeMidde(node):
    if node == None or node.next == None:
        return node
    node.value = node.next.value
    node.next = node.next.next

ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
removeMidde(middle_node)
print(ll)