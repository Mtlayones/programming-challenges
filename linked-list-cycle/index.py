from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        self.nodes = set()
        while head:
            if head == None:
                return False
            if head in self.nodes:
                return True
            self.nodes.add(head)
            head = head.next
