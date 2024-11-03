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
    
    if head.next is None:
        return deleteStart(head)

    current = head

    while current.next.next is not None:
        current = current.next

    current.next = None

    return head

def deleteAtPos(head, pos) -> Node:
    if pos < 0:
        return head
    
    if pos == 0:
        return deleteStart(head)
    
    cursor = 0
    current = head

    while cursor < pos - 1 and current.next.next is not None:
        cursor += 1
        current = current.next

    temp = current.next.next
    current.next = temp
    temp.next = current.next.next

    return head

    
def list_to_array(head: Optional[Node]) -> list:
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

class TestClass:
    def test_delete_start_with_1_node(self):
        head = Node(1)
        assert list_to_array(deleteStart(head)) == []
        
    def test_delete_start_with_multiple_nodes(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        assert list_to_array(deleteStart(head)) == [2, 3]
        
    def test_delete_end_with_1_node(self):
        head = Node(2)
        assert list_to_array(deleteEnd(head)) == []
        
    def test_delete_end_with_multiple_nodes(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        assert list_to_array(deleteEnd(head)) == [1, 2]

    def test_delete_at_position(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)

        assert list_to_array(deleteAtPos(head, 2)) == [1, 2, 4]