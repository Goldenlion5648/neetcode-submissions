# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        ret = ListNode()
        cur = ret
        while l1 or l2 or carry:
            cur.next = ListNode()
            cur = cur.next
            first_val = l1.val if l1 else 0
            second_val = l2.val if l2 else 0
            carry, cur.val = divmod(first_val + second_val + carry, 10)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return ret.next
