class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insertEnd(self, data):
        new_node = Node(data)
        if self.head is None:   # if list is empty
            self.head = new_node
        else:
            temp = self.head
            while temp.next:    # go to last node
                temp = temp.next
            temp.next = new_node

    # Insert at start
    def insertStart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Sort list
    def sortList(self):
        if self.head is None:
            return
        temp1 = self.head
        while temp1:
            temp2 = temp1.next
            while temp2:
                if temp1.data > temp2.data:   # swap data
                    temp1.data, temp2.data = temp2.data, temp1.data
                temp2 = temp2.next
            temp1 = temp1.next

    # Reverse list
    def reverseList(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    # Count nodes
    def countNodes(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    # Search element
    def search(self, key):
        temp = self.head
        pos = 0
        while temp:
            if temp.data == key:
                return pos
            temp = temp.next
            pos += 1
        return -1

    # Delete at specific position
    def deleteAtPos(self, pos):
        if self.head is None:
            return
        temp = self.head

        if pos == 0:  # delete first node
            self.head = temp.next
            return

        prev = None
        count = 0
        while temp and count != pos:
            prev = temp
            temp = temp.next
            count += 1

        if temp:  # delete node
            prev.next = temp.next

    # Delete entire list
    def deleteList(self):
        self.head = None

    # Display list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# ---------------- MENU ---------------- #
ll = LinkedList()

while True:
    print("\n------ MENU ------")
    print("1. Insert at End")
    print("2. Insert at Start")
    print("3. Sort List")
    print("4. Reverse List")
    print("5. Count Nodes")
    print("6. Search Element")
    print("7. Delete at Position")
    print("8. Delete Entire List")
    print("9. Display List")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter value: "))
        ll.insertEnd(data)

    elif choice == 2:
        data = int(input("Enter value: "))
        ll.insertStart(data)

    elif choice == 3:
        ll.sortList()
        print("List sorted.")

    elif choice == 4:
        ll.reverseList()
        print("List reversed.")

    elif choice == 5:
        print("Total nodes:", ll.countNodes())

    elif choice == 6:
        key = int(input("Enter element to search: "))
        pos = ll.search(key)
        if pos != -1:
            print(f"Element found at position {pos}")
        else:
            print("Element not found.")

    elif choice == 7:
        pos = int(input("Enter position to delete: "))
        ll.deleteAtPos(pos)

    elif choice == 8:
        ll.deleteList()
        print("List deleted.")

    elif choice == 9:
        ll.display()

    elif choice == 0:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
