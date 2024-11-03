export class Node {
  value: number;
  next: Node | null;

  constructor(value: number, next: Node | null = null) {
    this.value = value;
    this.next = next;
  }
}

export function InsertNewNode(
  head: Node | null,
  value: number,
  position: number
): Node | null {
  const newNode = new Node(value);
  if (head === null) {
    return position === 1 ? newNode : null;
  }

  if (position === 1) {
    newNode.next = head;
    return newNode;
  }

  let current = head;
  let cursor = 1;
  let length = 1;

  while (current.next !== null) {
    length++;
    current = current.next;
  }

  if (position <= length + 1) {
    current = head;
    cursor = 1;

    while (cursor < position - 1) {
      current = current.next!;
      cursor++;
    }

    newNode.next = current.next;
    current.next = newNode;
  }

  return head;
}

export function RemoveNodeAtPosition(
  head: Node | null,
  position: number
): Node | null {
  if (head === null) {
    return null;
  }

  if (position === 1) {
    return head.next;
  }

  let current: Node | null = head;
  let cursor = 1;

  while (cursor < position - 1 && current !== null) {
    current = current.next;
    cursor++;
  }

  if (current !== null && current.next !== null) {
    current.next = current.next.next;
  }

  return head;
}
