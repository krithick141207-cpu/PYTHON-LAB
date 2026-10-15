n = int(input("Enter no of elements:"))
a = list(map(int, input("Enter elements:").split()))
x = int(input("Enter element to search:"))

found = False
for i in range(n):
    if a[i] == x:
        found = True
        break

if found:
    print("Linear Search: Rollno found")
else:
    print("Linear Search: Rollno not found")

a.sort()
low = 0
high = n - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if a[mid] == x:
        found = True
        break
    elif a[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Binary Search: Rollno found")
else:
    print("Binary Search: Rollno not found")