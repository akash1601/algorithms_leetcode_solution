#zigzag level order

def zigzagOrder(root):
	res = []
	self.dfs(res, 0, root)
	return res
def dfs(self, res, level, node):
	if not node:
		return
	if level >= len(res):
		res.append([node.val])
	elif level % 2 == 0:
		res[level].extend([node.val])
	else:
		res[level].insert(0,node.val)
	for child in [node.left, node.right]:
		self.dfs(res, level + 1, child)