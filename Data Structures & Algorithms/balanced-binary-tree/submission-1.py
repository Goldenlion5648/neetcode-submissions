# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ret = True
        def get_depth(cur):
            nonlocal ret
            if not cur:
                return 0
            left = get_depth(cur.left)
            right = get_depth(cur.right)
            if abs(left - right) > 1:
                ret = False
                return 0
            return 1 + max(left, right)
        get_depth(root)
        return ret