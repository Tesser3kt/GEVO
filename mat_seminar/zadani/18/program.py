class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.root = None
        self.last = None

    def append(self, value):
        if not self.root:
            self.root = Node(value)
            self.last = self.root
        else:
            self.last.next = Node(value)
            self.last = self.last.next

    def prepend(self, value):
        # sem piste svuj kod
