import { describe, expect, it } from "vitest";
import { Node } from ".";
import { InsertNewNode, RemoveNodeAtPosition } from ".";

function listToArray(head: Node | null): number[] {
  const result: number[] = [];
  let current = head;
  while (current) {
    result.push(current.value);
    current = current.next;
  }
  return result;
}

describe("", () => {
  it("should return 101 -> 103 for test case 1", () => {
    let head: Node | null = null;
    head = InsertNewNode(head, 101, 1);
    head = InsertNewNode(head, 102, 2);
    head = InsertNewNode(head, 103, 2);
    head = RemoveNodeAtPosition(head, 3);
    expect(listToArray(head)).toStrictEqual([101, 103]);
  });
  it("should return 202 -> 201 for test cas 2", () => {
    let head: Node | null = null;
    head = InsertNewNode(head, 201, 1);
    head = InsertNewNode(head, 202, 1);
    head = RemoveNodeAtPosition(head, 3);
    expect(listToArray(head)).toStrictEqual([202, 201]);
  });
  it("should return 301 -> 302 for test cas 3", () => {
    let head: Node | null = null;
    head = InsertNewNode(head, 301, 1);
    head = InsertNewNode(head, 302, 2);
    head = InsertNewNode(head, 303, 4);
    expect(listToArray(head)).toStrictEqual([301, 302]);
  });
});
