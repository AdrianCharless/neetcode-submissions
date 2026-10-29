# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        secondStart = head

        if not head:
            return None
        node = head
        while node.next and node.next.next:
            secondStart = secondStart.next
            node = node.next.next
        nxt = secondStart.next
        secondStart.next = None
        secondStart = nxt

        node = secondStart
        prev = None

        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        secondStart = prev
        firstStart = head


        while secondStart:
            tmp1, tmp2 = firstStart.next, secondStart.next
            firstStart.next = secondStart
            secondStart.next = tmp1
            firstStart, secondStart = tmp1, tmp2



        # need to reverse second start to end

        