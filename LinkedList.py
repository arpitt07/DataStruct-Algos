
class Node:
    # defining nodes.
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

    #traverse through the list
    def printit(self):
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

    #removing an element
    def removeElement(self, remove_elm):
        temp = self.headval
        if temp is not None:
            if temp.dataval == remove_elm:
                self.headval = temp.nextval
                temp = None
                return

        while temp is not None:
            if temp.dataval == remove_elm:
                break
            prev = temp
            temp = temp.nextval

        if temp == None:
            print("None found")
            return

        prev.nextval = temp.nextval
        temp = None


list1 = SLinkedList()

list1.headval = Node("Monday")
list1.atBegining("Tuesday")
list1.atEnd("Friday")
list1.inBetween(list1.headval.nextval, "random")

list1.removeElement("random")
list1.printit()
