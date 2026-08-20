class Node:
    def __init__(self, name, time, purpose):
        self.name = name
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, name, time, purpose):
        new_node = Node(name, time, purpose)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if name <= current.name:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
    def search(self, name):
        current = self.root
        while current is not None:
            if name == current.name:
                print("Visitor Found")
                print("Name:", current.name)
                print("Entry Time:", current.time)
                print("Purpose:", current.purpose)
                return
            if name < current.name:
                current = current.left
            else:
                current = current.right
        print("Visitor Not Found")
    def delete(self, name):
        self.root = self.delete_node(self.root, name)
    def delete_node(self, root, name):
        if root is None:
            return root
        if name < root.name:
            root.left = self.delete_node(root.left, name)
        elif name > root.name:
            root.right = self.delete_node(root.right, name)
        else:
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            temp = root.right
            while temp.left is not None:
                temp = temp.left
            root.name = temp.name
            root.time = temp.time
            root.purpose = temp.purpose
            root.right = self.delete_node(root.right, temp.name)
        return root
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.name, root.time, root.purpose)
            self.inorder(root.right)
    def preorder(self, root):
        if root is not None:
            print(root.name, root.time, root.purpose)
            self.preorder(root.left)
            self.preorder(root.right)
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.name, root.time, root.purpose)
    def count(self, root):
        if root is None:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
bst = BST()
while True:
    print("1. Insert Log Entry")
    print("2. Search Log Entry")
    print("3. Delete Log Entry")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Count Total Entries")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Visitor Name: ")
        time = input("Enter Entry Time: ")
        purpose = input("Enter Purpose: ")
        bst.insert(name, time, purpose)
        print("Log Entry Inserted")
    elif choice == 2:
        name = input("Enter Visitor Name to Search: ")
        bst.search(name)
    elif choice == 3:
        name = input("Enter Visitor Name to Delete: ")
        bst.delete(name)
        print("Log Entry Deleted")
    elif choice == 4:
        print("\nInorder Traversal:")
        bst.inorder(bst.root)
    elif choice == 5:
        print("\nPreorder Traversal:")
        bst.preorder(bst.root)
    elif choice == 6:
        print("\nPostorder Traversal:")
        bst.postorder(bst.root)
    elif choice == 7:
        print("Total Entries:", bst.count(bst.root))
    elif choice == 8:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")

