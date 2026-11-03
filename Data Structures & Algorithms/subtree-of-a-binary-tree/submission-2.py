# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(cur_root):
            if cur_root is None:
                return False
            if is_same(cur_root, subRoot):
                return True
            return dfs(cur_root.left) or dfs(cur_root.right)
        
        def is_same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and is_same(p.left, q.left) and is_same(p.right, q.right)
        
        return dfs(root)
    