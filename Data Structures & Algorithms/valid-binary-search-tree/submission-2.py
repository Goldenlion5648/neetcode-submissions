# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(cur, lower_bound, upper_bound):
            if not cur:
                return True
            if not lower_bound < cur.val < upper_bound:
                return False
            if check(cur.left, lower_bound, min(upper_bound, cur.val)) and \
                check(cur.right, max(lower_bound, cur.val), upper_bound):
                return True
            return False
        return check(root, -math.inf, math.inf)