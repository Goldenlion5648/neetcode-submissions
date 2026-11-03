# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 2 3 4
    ^
        ^
'''
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast:
            fast = fast.next
            slow = slow.next
            if not fast:
                return slow
            fast = fast.next
        return slow


