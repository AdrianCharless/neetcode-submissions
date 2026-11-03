# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        len = 0
        while node:
            node = node.next
            len += 1
        
        nFromStart = len - n
        print(nFromStart)
        i = 0
        prev = None
        node = head
        while i < nFromStart:
            prev = node
            node = node.next
            i += 1
        if prev:
            prev.next = node.next
        else:
            head = head.next
        
        return head





