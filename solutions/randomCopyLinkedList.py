class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def randomCopy(head):
    	if not head:
    		return head

    	clones = {}
    	curr = head
    	while curr:
    		clones[curr] = Node(curr.val)
    		curr = curr.next

    	curr = head
    	while curr:
    		if curr.next:
    			clones[curr].next = clones[curr.next]
    		if curr.random:
    			clones[curr].random = clones[curr.random]
    		curr = curr.next
    	return clones[head]
