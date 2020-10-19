class Node:

    def __init__(self):# used to create Node
        self.leaft = None
        self.right = None
        self.data = data

    def insertData(self,value): #inseret Data and comparing data
        if self.data:
            if value > self.data:
                if self.leaft is None:
                    self.leaft = Node(value)
                else:
                    self.leaft.insert(value)
                elif value < self.data:
                    if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)


    def search(self):  # sued To serach tree

    def PrintTree(self): # used To print All node
        if self.leaft:
            self.leaft.PrintTree()
            print(self.data)
            self.right.Printtree()

root = Node(12)
