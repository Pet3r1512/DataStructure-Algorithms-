import { describe, expect, it } from "vitest";
import { insertAtEnd, insertAtPosition, ListNode } from ".";

function listToArray(head: ListNode | null): number[] {
  const result: number[] = [];
  let current = head;
  while (current) {
    result.push(current.value);
    current = current.next;
  }
  return result;
}

describe("Insert new node at the end of Linked list", () => {
  it("should return [1, 2, 3, 4] when input is head = [1, 2, 3] and value is 4", () => {
    const head = new ListNode(1, new ListNode(2, new ListNode(3)));
    const result = insertAtEnd(head, 4);
    expect(listToArray(result)).toStrictEqual([1, 2, 3, 4]);
  });
  it("should return 1 when input is empty list", () => {
    const head = null;
    const result = insertAtEnd(head, 1);
    expect(listToArray(result)).toStrictEqual([1]);
  });
});

describe("Insert new node at a specific position", () => {
  it("should return [1, 2, 4, 3] when head = [1, 2, 3] and position = 2 and value = 4", () => {
    const head = new ListNode(1, new ListNode(2, new ListNode(3)));
    const result = insertAtPosition(head, 2, 4);
    expect(listToArray(result)).toStrictEqual([1, 2, 4, 3]);
  });
  it("should return [1, 2, 3, 4] when head = [1, 2, 3] and position = 5 and value = 4", () => {
    const head = new ListNode(1, new ListNode(2, new ListNode(3)));
    const result = insertAtPosition(head, 4, 4);
    expect(listToArray(result)).toStrictEqual([1, 2, 3]);
  });
});
