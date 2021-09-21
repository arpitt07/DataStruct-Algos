class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def findval(self, val):
        if val < self.data:
            if self.left is None:
                return str(val)+" Not found"
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return str(val)+" Not found."
            return self.right.findval(val)
        else:
            print(str(self.data) + ' is found')

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.printTree()
print(root.findval(7))
print(root.findval(14))