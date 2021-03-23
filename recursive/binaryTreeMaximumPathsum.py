# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.total = float('-inf') 
        self.dfs(root)
        return self.total
    
    def dfs(self, root):
        if not root:
            return 0
        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)
        print(left)
        self.total = max(self.total, left + right + root.val)
        
        return max(left, right) + root.val