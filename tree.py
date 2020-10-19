class Node:

    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


    def insert(self,value):

        if self.data :  # used to parent nods
            if value > self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value < self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
       

    def printtree(self):
        if self.left:
            self.left.printtree()
            print(self.data)
        elif self.right:
            self.right.printtree()

root = Node(12)
root.insert(3)
root.insert(4)
root.insert(5)
root.printtree()







