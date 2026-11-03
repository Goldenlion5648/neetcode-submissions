# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 4 5 6
  P
    C
      A

edge case:
when L == R
L != 1
R == len(list)
'''
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pos = 1
        prev = ListNode(-1, head)
        ret = prev
        cur: ListNode = head
        while pos < left:
            prev = cur
            cur = cur.next
            pos += 1
        before_list = prev
        while pos < right:
            cur = cur.next
            pos += 1
        
        after_list = cur.next
        prev = before_list
        cur = before_list.next
        left_end = cur
        for i in range(right + 1 - left):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        # print(cur)
        before_list.next = prev
        left_end.next = after_list
        return ret.next














