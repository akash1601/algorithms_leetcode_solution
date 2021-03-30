# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        self.dfs(root, [])
        self.ans = []
        for path in self.res:
            newPath = "->".join(path)
            self.ans.append(newPath)
        return self.ans
        
    def dfs(self,root, ls):
        if not root:
            return False
        if not root.left and not root.right:
            ls.append(str(root.val))
            self.res.append(ls)
        self.dfs(root.left, ls+[str(root.val)])
        self.dfs(root.right, ls+[str(root.val)])
        