MAX = 100
stack = []
def push():
    if len(stack) >= MAX:
        print("Stack Overflow")
    else:
        book = input("Enter book title to push: ")
        stack.append(book)
        print(book, "added to stack")
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        book = stack.pop()
        print(book, "removed from stack")
def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Books in Stack:")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])
n = int(input("Enter number of books: "))
for i in range(n):
    push()
print("\nStack after Push:")
display()
choice = int(input("\nEnter choice (1-Push, 2-Pop): "))
if choice == 1:
    push()
elif choice == 2:
    pop()
else:
    print("Invalid choice")
print("\nFinal Stack:")
display()
