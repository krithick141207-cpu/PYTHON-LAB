class EnrollmentNode:
    def __init__(self, enrollment_id, student_name, course_name):
        self.enrollment_id = enrollment_id
        self.student_name = student_name
        self.course_name = course_name
        self.height = 1
        self.left = None
        self.right = None
def height(node):
    if node is None:
        return 0
    return node.height
def get_balance(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)
def right_rotate(y):
    x = y.left
    temp = x.right
    x.right = y
    y.left = temp
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x
def left_rotate(x):
    y = x.right
    temp = y.left
    y.left = x
    x.right = temp
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y
def insert(root, enrollment_id, student_name, course_name):
    if root is None:
        return EnrollmentNode(
            enrollment_id,
            student_name,
            course_name
        )
    if enrollment_id < root.enrollment_id:
        root.left = insert(
            root.left,
            enrollment_id,
            student_name,
            course_name
        )
    elif enrollment_id > root.enrollment_id:
        root.right = insert(
            root.right,
            enrollment_id,
            student_name,
            course_name
        )
    else:
        print("Enrollment ID already exists!")
        return root
    root.height = 1 + max(
        height(root.left),
        height(root.right)
    )
    balance = get_balance(root)
    if balance > 1 and enrollment_id < root.left.enrollment_id:
        return right_rotate(root)
    if balance < -1 and enrollment_id > root.right.enrollment_id:
        return left_rotate(root)
    if balance > 1 and enrollment_id > root.left.enrollment_id:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and enrollment_id < root.right.enrollment_id:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root
def min_value_node(root):
    current = root
    while current.left is not None:
        current = current.left
    return current
def delete(root, enrollment_id):
    if root is None:
        return root
    if enrollment_id < root.enrollment_id:
        root.left = delete(root.left, enrollment_id)
    elif enrollment_id > root.enrollment_id:
        root.right = delete(root.right, enrollment_id)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = min_value_node(root.right)
        root.enrollment_id = temp.enrollment_id
        root.student_name = temp.student_name
        root.course_name = temp.course_name
        root.right = delete(
            root.right,
            temp.enrollment_id
        )
    root.height = 1 + max(
        height(root.left),
        height(root.right)
    )
    balance = get_balance(root)
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root
def search(root, enrollment_id):
    if root is None:
        return None
    if enrollment_id == root.enrollment_id:
        return root
    if enrollment_id < root.enrollment_id:
        return search(root.left, enrollment_id)
    return search(root.right, enrollment_id)
def inorder(root):
    if root:
        inorder(root.left)
        print(
            "Enrollment ID:", root.enrollment_id,
            "| Student:", root.student_name,
            "| Course:", root.course_name
        )
        inorder(root.right)
def count_enrollments(root):
    if root is None:
        return 0
    return (
        1
        + count_enrollments(root.left)
        + count_enrollments(root.right)
    )
root = None
while True:
    print("1. Insert Enrollment")
    print("2. Delete Enrollment")
    print("3. Search Enrollment")
    print("4. Display All Enrollments")
    print("5. Count Total Enrollments")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enrollment_id = int(input("Enter Enrollment ID: "))
        student_name = input("Enter Student Name: ")
        course_name = input("Enter Course Name: ")
        root = insert(
            root,
            enrollment_id,
            student_name,
            course_name
        )
        print("Enrollment inserted successfully.")
    elif choice == 2:
        enrollment_id = int(
            input("Enter Enrollment ID to delete: ")
        )
        if search(root, enrollment_id):
            root = delete(root, enrollment_id)
            print("Enrollment deleted successfully.")
        else:
            print("Enrollment not found.")
    elif choice == 3:
        enrollment_id = int(
            input("Enter Enrollment ID to search: ")
        )
        result = search(root, enrollment_id)
        if result:
            print("\nEnrollment Found")
            print("Enrollment ID:", result.enrollment_id)
            print("Student Name:", result.student_name)
            print("Course Name:", result.course_name)
        else:
            print("Enrollment not found.")
    elif choice == 4:
        print("\nAll Enrollments in Sorted Order:")
        inorder(root)
    elif choice == 5:
        total = count_enrollments(root)
        print("Total Enrollments:", total)
    elif choice == 6:
        print("Program ended.")
        break
    else:
        print("Invalid choice!")

