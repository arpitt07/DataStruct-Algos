
class Node:
    # defining nodes.
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    #traverse through the list
    def search(self):
        val = self.headval
        while val is not None:
            print(val.dataval)
            val = val.nextval

    #function to insert a new element in the begining
    def atBegining(self, newdata):
        newNode = Node(newdata)

        #updating the new nodes next value to the existing node
        newNode.nextval = self.headval
        self.headval = newNode

    #function to insert a new element in the end
    def atEnd(self, enddata):
        endNode = Node(enddata)
        #check to ensure there is a headval
        if self.headval is None:
            self.headval = endNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = endNode

    #inserting a new element in between
    def inBetween(self, mid_node,  middata):
        if mid_node is None:
            return

        #kinda like building a swap here
        midnode = Node(middata)
        midnode.nextval = mid_node.nextval
        mid_node.nextval = midnode


list1 = SLinkedList()
list1.headval = Node("Monday")

e2 = Node("Tuesday")
e3 = Node("Wednesday")

#connect the nodes
list1.headval.nextval = e2

e2.nextval = e3



list1.inBetween(list1.headval.nextval, "random")
list1.search()