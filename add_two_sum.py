# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1Multiplier = 1
        l2Multiplier = 1
        l1Num = 0
        l2Num = 0
        while l1 != None:
            l1Num += l1.val * l1Multiplier
            l1Multiplier *= 10
            l1 = l1.next
        while l2 != None:
            l2Num += l2.val * l2Multiplier
            l2Multiplier *= 10
            l2 = l2.next
        total = l1Num + l2Num
        totalArray = list("{}".format(total))
        listNode = ListNode(val=totalArray[-1], next=None)
        placeholder = listNode
        for x in range(len(totalArray)-2, -1, -1):
            listNode.next = ListNode(val=totalArray[x], next=None)
            listNode = listNode.next
        return placeholder
