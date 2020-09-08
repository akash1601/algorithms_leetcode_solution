class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(n, level=0, res=[]):
            if not n:
                return
            if level >= len(res):
                res.append([n.val])
            else:
                res[level].append(n.val)
            for child in [n.left, n.right]:
                dfs(child, level=level+1)
            return res

        return dfs(root)
        