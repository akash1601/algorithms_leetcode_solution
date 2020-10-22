# build bst using inorder and preorder
def buildingTree(preorder, inorder):
	if inorder:
		ind = inorder.index(preorder.pop(0))
		root = TreeNode(ind)
		root.left = self.buildingTree(preorder, inorder[0:ind])
		root.right = self.buildingTree(preorder, inorder[ind+1:])
		return 