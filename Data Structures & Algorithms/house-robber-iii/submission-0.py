# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import functools
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @functools.cache
        def dfs(cur, is_skipped):
            if not cur:
                return 0
            self_val = cur.val if not is_skipped else 0
            options = []
            if is_skipped:
                options.append(dfs(cur.left, False) + dfs(cur.right, False))
            else:
                options.append(cur.val + dfs(cur.left, True) + dfs(cur.right, True))
                options.append(dfs(cur.left, False) + dfs(cur.right, False))
            return max(options)
        return dfs(root, False)
