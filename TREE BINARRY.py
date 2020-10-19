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



    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


   # """"def inorderTraversal(self, root):
    #    res = []
     #   if root:
      #      res = self.inorderTraversal(root.left)
       #     res.append(root.data)
        #    res = res + self.inorderTraversal(root.right)
        #return res""""

    def preorder(self,root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder(root.left)
            print(res)
            res = res + self.preorder(root.right)
        return res





if __name__ == '__main__':
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
   # root.PrintTree()
    #print(root.inorderTraversal(root))
    print(root.preorder(root))



