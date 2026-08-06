text = input("Enter a string: ")

clean = ""

for ch in text:
 if ch.isalnum():
    clean += ch.lower()

stack = []
queue = []

for ch in clean:
    stack.append(ch)
    queue.append(ch)

palindrome = True

while len(stack) > 0:
    if stack.pop() != queue.pop(0):
        palindrome = False
    break

if palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")
