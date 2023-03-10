from typing import Optional
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        prev_temp = head
        while temp != None:
            if temp.val == val and temp == head:
                head = temp.next
            elif temp.val == val:
                prev_temp.next = temp.next
            else:
                prev_temp = temp
            temp = temp.next
        return head
