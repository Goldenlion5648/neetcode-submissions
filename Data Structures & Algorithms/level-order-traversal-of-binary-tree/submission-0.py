# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        def dfs(cur, depth):
            if not cur:
                return
            if depth >= len(ret):
                ret.append([])
            ret[depth].append(cur.val)
            dfs(cur.left, depth + 1)
            dfs(cur.right, depth + 1)
        dfs(root, 0)
        return ret