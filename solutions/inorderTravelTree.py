def inorderTravel(self, root):
	res = []
	self.helper(root, res)
	return res

def helper(node, res):
	if node:
		self.helper(root.left, res)
		res.append(node.val)
		self.helper(root.right, res)