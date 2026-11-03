# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ret = 0
        def dfs(cur, highest_seen=None):
            nonlocal ret
            if not cur:
                return
            if highest_seen is None:
                highest_seen = cur.val
            highest_seen = max(highest_seen, cur.val) 
            if highest_seen <= cur.val:
                ret += 1
            dfs(cur.left, highest_seen)
            dfs(cur.right, highest_seen)
        dfs(root)
        return ret

