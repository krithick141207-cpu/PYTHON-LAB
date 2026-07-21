class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,item):
        new_node=Node(item)
        new_node.next=self.top
        self.top=new_node
        print(item,"Pushed into stock")
    def pop(self):
        if self.top is None:
            print("stack underflow")
            return None
        popped=self.top.data
        self.top=self.top.next
        print(popped,"popped from stack")
        return popped
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        temp=self.top
        print("stack elements:")
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()
s=Stack()
while True:
    print("\n1.push")
    print("2.pop")
    print("3.display")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        item=input("enter book title:")
        s.push(item)
    elif choice==2:
        s.pop()
    elif choice==3:
        s.display()
    elif choice==3:
        print("Exiting...")
        break
    else:
        print("Invalid choice")