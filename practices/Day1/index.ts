export class ListNode {
  value: number;
  next: ListNode | null;

  constructor(value: number, next: ListNode | null = null) {
    this.value = value;
    this.next = next;
  }
}

export function insertAtEnd(head: ListNode | null, value: number): ListNode {
  const newNode = new ListNode(value);

  if (head === null) {
    return newNode;
  }

  let current = head;
  while (current.next !== null) {
    current = current.next;
  }

  current.next = newNode;

  return head;
}

export function insertAtPosition(
  head: ListNode,
  position: number,
  value: number
): ListNode {
  if (position < 0) {
    return head;
  }

  const newNode = new ListNode(value);

  if (position === 0) {
    newNode.next = head;
    head = newNode;
  }

  let cursor = 1;
  let current = head;

  while (cursor < position && current.next !== null) {
    current = current.next;
    cursor++;
  }

  if (cursor < position) {
    return head;
  }

  newNode.next = current.next;
  current.next = newNode;

  return head;
}
