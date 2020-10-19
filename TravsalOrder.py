class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def inorder(root): # L->Root->Right
        if root:
            inorder(root.left)
            print(data)
            inorder(root.right)