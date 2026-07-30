class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    def insert(self, coeff, power):
        new = Node(coeff, power)

        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.coeff}x^{temp.power}", end="")
            if temp.next:
                print(" + ", end="")
            temp = temp.next
        print()


def add(poly1, poly2):
    p = poly1.head
    q = poly2.head
    result = Polynomial()

    while p and q:
        if p.power == q.power:
            result.insert(p.coeff + q.coeff, p.power)
            p = p.next
            q = q.next

        elif p.power > q.power:
            result.insert(p.coeff, p.power)
            p = p.next

        else:
            result.insert(q.coeff, q.power)
            q = q.next

    while p:
        result.insert(p.coeff, p.power)
        p = p.next

    while q:
        result.insert(q.coeff, q.power)
        q = q.next

    return result


poly1 = Polynomial()
poly2 = Polynomial()

n1 = int(input("Enter number of terms in Polynomial 1: "))
print("Enter coefficient and power:")
for i in range(n1):
    c, p = map(int, input().split())
    poly1.insert(c, p)

n2 = int(input("Enter number of terms in Polynomial 2: "))
print("Enter coefficient and power:")
for i in range(n2):
    c, p = map(int, input().split())
    poly2.insert(c, p)

print("\nPolynomial 1:")
poly1.display()

print("Polynomial 2:")
poly2.display()

result = add(poly1, poly2)

print("Resultant Polynomial:")
result.display()