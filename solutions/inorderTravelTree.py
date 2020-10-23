def inorderTravel(self, root):
	res = []
	self.helper(root, res)
	return res

def helper(node, res):
	if node:
		self.helper(root.left, res)
		res.append(node.val)
		self.helper(root.right, res)

#postorder traverssal left -> right -> Node
def postorderTravel(self, root):
	res = []
	self.helper(root, res)
	return res

def helper(node, res):
	if node:
		self.helper(root.left, res)
		self.helper(root.right, res)
		res.append(node.val)

#preorder  traversal Node -> left -> right
def postorderTravel(self, root):
	res = []
	self.helper(root, res)
	return res

def helper(node, res):
	if node:
		res.append(node.val)
		self.helper(root.left, res)
		self.helper(root.right, res)