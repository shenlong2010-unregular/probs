# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return "{}<-{}->{}".format(self.prev, self.value, self.next)

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return "Head {}\nTail {}".format(self.head, self.tail)
    #6 O(1) ST
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    #7 O(1) ST
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    #4 O(1) ST
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert
			
    #5 O(1) ST
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    #8 O(P) T, O(1) S
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # O(n) T, O(1) S
    def removeNodesWithValue(self, value):
        current = self.head
        while current is not None:
            nodeToRemove = current
            current = current.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    #3 O(1) ST
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    #1 O(N) time, O(1) space
    def containsNodeWithValue(self, value):
        current = self.head
        # check if the current is not None and the value not value
        while current is not None and current.value != value:
            current = current.next
        return current is not None

    #2 O(1) ST
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

first = Node(1)
second = Node(2)
third = Node(3)
myLink = DoublyLinkedList()
myLink.setHead(first)
myLink.insertAfter(first, second)
myLink.insertAfter(second, third)
