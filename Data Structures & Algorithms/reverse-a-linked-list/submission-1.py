# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
_ 4 5 6 7 
  P
 <  C
    A

'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prev = None
        cur = head
        while cur:
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        return prev
