from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return True
        length = 0
        temp = head
        while temp != None:
            length += 1
            temp = temp.next
        temp = head
        for itr in range(length//2):
            temp = temp.next
        if length % 2 == 1:
            temp = temp.next
        prevNode = None
        nextNode = None
        while temp != None:
            prevNode = temp
            temp = temp.next
            prevNode.next = nextNode
            nextNode = prevNode
        while prevNode != None:
            if prevNode.val != head.val:
                return False
            prevNode = prevNode.next
            head = head.next

        return True
