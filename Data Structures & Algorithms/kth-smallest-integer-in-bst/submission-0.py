# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        def dfs(cur):
            if not cur:
                return
            heapq.heappush_max(heap, cur.val)
            if len(heap) > k:
                heapq.heappop_max(heap)
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return heap[0]
