
class Stack:
    def __init__(self):
        self.stack = []

    #append an element
    def add(self, val):
        self.stack.append(val)

    # return the top element in the stack
    def peek(self):
        return self.stack[-1]

    #pop an element
    def remove(self):
        if len(self.stack) <= 0:
            return ("Stack is empty")
        else:
            self.stack.pop()

    def printstack(self):
        for i in self.stack:
            print(i)

d = Stack()
d.add(5)
d.add(8)
d.add(7)
d.add(9)
d.add(5)
#d.printstack()

d.remove()
print(d.peek())
