# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
    
        return self.pathSum(root.left, sum) + self.pathSum(root.right, sum) + self.innerPath(root, sum)
        
    def innerPath(self,root, sum):
        
        if root is None:
            return 0 
    
        res = 0
        if root.val == sum:
            res += 1
        res += self.innerPath(root.left, sum- root.val)
        res += self.innerPath(root.right, sum - root.val)
        return res  
            