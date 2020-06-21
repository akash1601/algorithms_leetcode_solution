def addTwoNum(l1,l2):
	a = curr = lIstNode(0)
	c = 0
	while l1 or l2 or c:
		v1 = v2 = 0
		if l1:

			v1 = l1.val
			l1 = l1.next

		if l2:

			v2 = l2.val
			l2 = l2.next

		total = v1 + v2 + c
		c = total // 10
		val =  total % 10
		curr.next = ListNode(val)
		curr = curr.next
	return a.next



