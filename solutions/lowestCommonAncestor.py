class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p ,q)
        right = self.lowestCommonAncestor(root.right,p ,q)
        if left is not None and right is not None:
            return root
        if any([left, right]) is not None:
            return left if left is not None else right 
        return None