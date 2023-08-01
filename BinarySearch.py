#class for the binary search tree and methods relating to it 
class binarySearch: 
    def __init__(self, data): 
        self.left = None
        self.right = None
        self.data = data
    
    #method to add new key to binary search tree
    def insert(self, data): 
        if self.data:
            if data < self.data: 
                if self.left is None: 
                    self.left = binarySearch(data)
                else: 
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = binarySearch(data)
                else: 
                    self.right.insert(data)
        else:
            self.data = data

    #method to print binary search tree
    def printNodeTree(self): 
        if self.left: 
            self.left.printNodeTree()
        print(self.data),
        if self.right:
            self.right.printNodeTree()
    
    #method to traverse the binary search tree 
    def traversal(self, root): 
        res = []
        if root: 
            res = self.traversal(root.left)
            res.append(root.data)
            res = res + self.traversal(root.right)
        return res 

    #method to search through the binary search tree
    def search(self, data): 
        if self.data == data: 
            print("\nThe searched item is found!")
            print(self.data)
            return True
        if data < self.data:
            if self.left == None:
                print("\nThe searched item is not found!")
                return False
            return self.left.search(data)
        if self.right == None:
            print("\nThe searched item is not found!")
            return False
        return self.right.search(data)

    
