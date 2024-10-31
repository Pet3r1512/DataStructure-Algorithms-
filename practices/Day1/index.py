from typing import Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insertEnd(head: Node, value: int) -> Node:
    newNode = Node(value)

    if head is None:
        return newNode

    current = head

    while current.next is not None:
        current = current.next

    current.next = newNode
    
    return head

def list_to_array(head: Optional[Node]) -> list:
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

def test():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    result = insertEnd(head, 4)
    assert list_to_array(result) == [1, 2, 3, 4]