
class Queue:
    def __init__(self):
        self.queue = list()

    # add an element only if its unique
    def add(self, val):
        if val not in self.queue:
            self.queue.insert(0, val)
            return True
        else:
            return False

    def remove(self):
        if len(self.queue) > 0:
            self.queue.pop()
        return ("queue is empty")

    def printqueue(self):
        for i in self.queue:
            print(i)

d = Queue()

d.add(5)
d.add(7)
d.add(1)
d.printqueue()
d.remove()
print(d.remove())
