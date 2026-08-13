class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def insert(root,data):
    if root is None:
        return Node(data)
    if data<root.data:
        root.left=insert(root.left,data)
    else:
        root.right=insert(root.right,data)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
root=None
n=int(input("Enter number of book titles:"))
for i in range(n):
    title=input("Enter book title:")
    root=insert(root,title)
print("Book titles in order Traversal:")
inorder(root)