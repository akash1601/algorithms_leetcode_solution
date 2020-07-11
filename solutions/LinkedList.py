class Node:
	def __init__(self,val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		
		temp = self.head
		while(temp):

			print(temp.val)
			temp = temp.next

	def insertList(self,n):
		
		temp = self.head
		while(temp):
			if temp.val == None:
				four = Node(n)
				temp.val = n
				temp.next = None
			
			temp = temp.next

		

	

list = LinkedList()
list.head = Node(1)
second = Node(2)
third = Node(3)
list.head.next = second
second.next = third
list.printList()
list.insertList(4)
list.printList()

