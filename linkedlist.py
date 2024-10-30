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

    insertEndValue = input("Enter your value to be inserted in the linked list: ")
    insert_at_the_end(head, int(insertEndValue))
    
    return head

head = main()
print("Linked list: ")
traversalLinkedList(head)