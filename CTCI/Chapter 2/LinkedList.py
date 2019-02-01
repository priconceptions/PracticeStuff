class Node:
    def __init__(self, value, nextNode=None, prevNode=None):
        self.value = value
        self.next = nextNode
        self.prev = prevNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, value):
        if self.head == None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(value)
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
    
    def traverse(self):
        ptr = self.head
        while ptr:
            yield ptr.value
    



