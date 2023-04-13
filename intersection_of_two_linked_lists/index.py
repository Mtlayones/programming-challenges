from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h_map = dict()
        while headA != None:
            if headA.val not in h_map.keys():
                h_map[headA.val] = [headA]
            else:
                h_map[headA.val].append(headA)
            headA = headA.next
        length = 0
        tempA = None
        tempB = None
        while headB != None:
            if headB.val in h_map.keys():
                length = len(h_map[headB.val])
                for i in range(length):
                    tempA = h_map[headB.val][i]
                    tempB = headB
                    while tempA != None and tempB != None:
                        if tempA != tempB:
                            break
                        tempA = tempA.next
                        tempB = tempB.next
                    if tempA == None and tempB == None:
                        return headB
            headB = headB.next
        return
