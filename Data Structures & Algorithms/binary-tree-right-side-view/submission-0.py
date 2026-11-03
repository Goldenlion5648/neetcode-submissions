# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        depth_to_seen = []
        def dfs(cur, depth):
            if not cur:
                return
            if depth == len(depth_to_seen):
                depth_to_seen.append(cur.val)
            else:
                depth_to_seen[depth] = cur.val
            dfs(cur.left, depth + 1)
            dfs(cur.right, depth + 1)
        dfs(root, 0)
        return depth_to_seen