from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prevNode = None
        nextNode = None
        temp = head
        while temp:
            nextNode = temp.next
            temp.next = prevNode
            prevNode = temp
            temp = nextNode
        return prevNode
