"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        ret = Node(-1)
        ret_runner = ret

        cur = head
        old_to_new = {None : None}
        while cur:
            ret_runner.next = Node(cur.val)
            ret_runner = ret_runner.next
            old_to_new[cur] = ret_runner
            cur = cur.next
        
        
        cur = head
        ret_runner = ret.next
        while cur:
            ret_runner.random = old_to_new[cur.random]
            
            ret_runner = ret_runner.next
            cur = cur.next
        return ret.next
        
        




















