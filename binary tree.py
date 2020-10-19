class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):

        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)


    def findval(self, value):
        if value < self.data:
            if self.left is None:
                return " Not Found"
            return self.left.findval(value)
        elif value > self.data:
            if self.right is None:
                return " Not Found"
            return self.right.findval(value)
        else:
            return(self.data)



    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

root = Node(12)
root.insert(2)
root.insert(14)
root.insert(3)
root.PrintTree()
print("#-------------------#")
print(root.findval(7))
print(root.findval(14))


