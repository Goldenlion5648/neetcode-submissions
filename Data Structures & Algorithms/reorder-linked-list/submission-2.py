# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        slow_prev = None
        while fast:
            slow_prev = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        if not slow_prev:
            return
        slow_prev.next = None

        prev = None
        cur = slow
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        left = head
        right = prev

        ret = head
        while left and right:
            old_left_next = left.next
            left.next = right
            if not old_left_next:
                break
            old_right_next = right.next
            right.next = old_left_next
            left = old_left_next
            right = old_right_next






