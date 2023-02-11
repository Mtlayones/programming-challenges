from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while head != None:
            if prev is not None and head.val == prev.val:
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return temp
