#class for individual nodes inside link list
class Node():
    def __init__(self, dataval=None): 
        self.dataval = dataval
        self.next = None

#class for the link list and methods relating to it
class linkList(): 
    def __init__(self):
        self.head = None
    
    #method to add new data at the end of the link list
    def addNode(self, newdata):
        NewNode = Node(newdata) 
        if self.head is None: 
            self.head = NewNode 
            return 
        laste = self.head 
        while (laste.next):
            laste = laste.next 
        laste.next = NewNode

    #method to remove a node from link list
    def deleteNode(self, Removekey):
        HeadVal = self.head

        if (HeadVal is not None): 
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
            
            while (HeadVal is not None):
                if HeadVal.data == Removekey:
                    break
                previous = HeadVal
                HeadVal = HeadVal.next

            if (HeadVal == None): 
                return
            
            previous.next = HeadVal.next
            HeadVal = None
            
    #method to print values inside the node
    def printNodeDetails(self): 
        printData = self.head
        while printData is not None: 
            print(printData.dataval)
            printData = printData.next

    #method to iterate the nodes in link list
    def iterateNode(self):
        item = self.head
        while item:
            value = item.dataval
            item = item.next
            yield value
