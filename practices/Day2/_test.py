from typing import Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def deleteStart(head) -> Node:
    if head is None:
        return None
    
    return head.next


def deleteEnd(head) -> Node:
    if head is None:
        return None

    current = head

    while current.next.next is not None:
        current = current.next

    current.next = None

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
    head.next.next.next = Node(4)
    result = deleteStart(head)
    assert list_to_array(result) == [2, 3, 4]
    result = deleteEnd(head)
    assert list_to_array(result) == [1, 2, 3]