# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        one = list1
        two = list2
        if one is None:
            return list2
        elif two is None:
            return list1
        if one and one.val < two.val:
            head = one
            one = one.next
        elif two:
            head = two
            two = two.next
        else:
            return list1

        prev = head
        while one != None or two != None:
            if not two or (one and one.val < two.val):
                prev.next = one
                prev = one
                one = one.next
            else:
                prev.next = two
                prev = two
                two = two.next
            
        return head


        