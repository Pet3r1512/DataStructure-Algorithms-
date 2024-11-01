# Single Linked List
# For each node, there are: data and pointer to next node
# For last node, the pointer will be NULL

# Define a Node 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


### Operations with Single Linked List

## Insertion: add new node to the linked list with 3 positions: head, end and specific position

# Insert new node at the beginning of linked list = head

def insert_at_beginning(head, value):
    # create a new node with given value
    newNode = Node(value)

    # set the next pointer = new node to current head
    newNode.next = head

    # move the head to new node
    head = newNode

    return head

# Insert new node at the end of linked list
def insert_at_the_end(head, value):
    # create a new node with given value
    newNode = Node(value)

    # if the linked list is empty, return new node
    if head is None:
        return newNode

    # if linked list is not empty
    current = head
    # tranverse the linked list until last node
    while current.next is not None:
        current = current.next

    # update last node's next is new node
    current.next = newNode

    return head

# Insert new Node at a specific position
def insert_at_specific_position(head, value, position):
    if position < 1:
        print("Invalid position")
        return head

    # if position is 1 then insert at the beginning
    if position == 1:
        newNode = Node(value)
        newNode.next = head
        return newNode

    # traverse linked list to the given position
    cursor = 1
    current = head
    while cursor < position - 1 and current is not None:
        current = current.next
        cursor += 1

    if current is None:
        print("Invalid position")
        return head
    
    # add new node
    newNode = Node(value)
    newNode.next = current.next
    current.next = newNode

    return head

## Deletion: delete a node with 3 positions: head, end and specific position

# Delete a node at the beginning of linked list

def delete_at_beginning(head):
    if head is None:
        return None
    
    temp = head
    head = head.next
    temp = None

    return head

# Delete a node at the end of linked list

def delete_at_end(head):
    if head is None:
        return None
    
    if head.next is None:
        return delete_at_beginning(head)

    current = head

    while current.next.next is not None:
        current = current.next

    current.next = None

    return head

# Delete a node at a specific position

def delete_at_position(head, position):
    if head is None:
        return None
    
    if position < 0:
        print("Invalid position")
        return head
    
    if position == 0:
        return delete_at_beginning(head)
    
    cursor = 0
    current = head

    for i in range(0, position - 1):
        if current is not None:
            current = current.next

    if current is None or current.next is None:
        print("Invalid position")
        return head

    temp = current.next
    current.next = current.next.next
    temp = None

    return head

## Traversal: visiting each node in linked list and perform some operations on the data

def traversalLinkedList(head):
    current = head

    while current is not None:
        # Print data of current node
        print(current.data, "->", end=" ") 
        # Move the cursor to next node in the linked list
        current = current.next
    print("null")
    print()

# Main function
def main():
    inputs = input("Enter your list: ")
    arr = inputs.split()
    head = None

    for number in arr:
        head = insert_at_beginning(head, int(number))
    
    traversalLinkedList(head)

    # insertEndValue = input("Enter your value to be inserted in the linked list: ")
    # insert_at_the_end(head, int(insertEndValue))

    # insertValue = input("Enter value u want to import: ")
    # position = input("And import at position: ")

    # head = insert_at_specific_position(head, int(insertValue), int(position))

    # head = delete_at_beginning(head)

    # traversalLinkedList(head)

    # head = delete_at_end(head)

    # traversalLinkedList(head)

    delPos = input("Enter position you want to delete, start from 0: ")

    head = delete_at_position(head, int(delPos))

    traversalLinkedList(head)
    
    return head

head = main()