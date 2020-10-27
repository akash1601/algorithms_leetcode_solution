#check for valid BST
    def validateBinary(root):
    	return self.checkBst(root, float("-inf"), float("inf"))

    def checkBst(node, left, right):
    	if not node:
    		return True

    	if not left < node.val < right:
    		return False

    	return (self.checkBst(node.left,left,node.val)) and (self.checkBst(node.right, node.val, right))