# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        else:
            slow = head
            fast = head.next

        while slow != None:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if fast and fast.next:
                    fast = fast.next.next
                else:
                    fast = None
        return False