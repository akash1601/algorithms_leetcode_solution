class ListNode:
   def __init__(self, x):
   	self.val = x
   	self.next = None
   	
def merge(l1,l2):
	if l1 and l2:
		if l1.val > l2.val:
			l1, l2 = l2, l1
		l1.next = self.merge(l1.next,l2)

	return l1 or l2

merge([1,2,3],[1,4,6])
