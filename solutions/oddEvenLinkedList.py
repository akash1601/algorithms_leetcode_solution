def oddEvenList(head):
	l1 = h1 = ListNode(0)
	l2 = h2 = ListNode(0)
	while head:
		l1.next = head
		l2.next = head
		l1 = l1.next
		l2 = l2.next
		if head.next:
			head = head.next.next
		else:
			head = None
	l1.next = h2.next
	return h1.next