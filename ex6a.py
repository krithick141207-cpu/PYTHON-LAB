def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:
        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:
            while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(ch):
                postfix += stack.pop()
            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix

expr = input("Enter Infix Expression: ")
print("Postfix Expression:", infix_to_postfix(expr))
