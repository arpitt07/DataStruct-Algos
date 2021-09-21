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

    def inOrderTraversal(self, root):
        output = []
        if root:
            output += self.inOrderTraversal(root.left)
            output.append(root.data)
            output += self.inOrderTraversal(root.right)
        return output

    def preOrderTraversal(self, root):
        output = []
        if root:
            output.append(root.data)
            output += self.preOrderTraversal(root.left)
            output += self.preOrderTraversal(root.right)
        return output

    def postOrderTraversal(self, root):
        output = []
        if root:
            output += self.postOrderTraversal(root.left)
            output += self.postOrderTraversal(root.right)
            output.append(root.data)
        return output


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.postOrderTraversal(root))