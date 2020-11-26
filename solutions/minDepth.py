class Solution:
    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return 0
        queue = []
        queue.append(root)
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth