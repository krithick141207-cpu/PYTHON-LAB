class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, job, priority):
        self.heap.append((priority, job))
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent][0] < self.heap[i][0]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break

    def extract_max(self):
        if not self.heap:
            print("Heap is empty")
            return

        max_job = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            i = 0

            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i

                if left < len(self.heap) and self.heap[left][0] > self.heap[largest][0]:
                    largest = left

                if right < len(self.heap) and self.heap[right][0] > self.heap[largest][0]:
                    largest = right

                if largest != i:
                    self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                    i = largest
                else:
                    break

        print("Processed Job:", max_job[1])
        print("Priority:", max_job[0])

    def peek(self):
        if not self.heap:
            print("Heap is empty")
        else:
            print("Highest Priority Job:", self.heap[0][1])
            print("Priority:", self.heap[0][0])

    def display(self):
        if not self.heap:
            print("Heap is empty")
        else:
            print("Jobs in Heap Order:")
            for priority, job in self.heap:
                print(job, "-", priority)


heap = MaxHeap()

while True:
    print("\n--- Job Scheduler Using Max Heap ---")
    print("1. Insert Job")
    print("2. Delete Highest Priority Job")
    print("3. Peek Highest Priority Job")
    print("4. Display All Jobs")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        job = input("Enter job name: ")
        priority = int(input("Enter priority: "))
        heap.insert(job, priority)
        print("Job inserted successfully")

    elif choice == 2:
        heap.extract_max()

    elif choice == 3:
        heap.peek()

    elif choice == 4:
        heap.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")
