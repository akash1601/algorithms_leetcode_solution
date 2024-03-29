# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node: return
            if low <= node.val <= high: self.out += node.val
            if node.val > low:  dfs(node.left)
            if node.val < high: dfs(node.right)
                
        self.out = 0
        dfs(root)
        return self.out