 def rotateRight(head,k):
    if not head:
        return None
        
    lastElement = head
    length = 1
    while ( lastElement.next ):
        lastElement = lastElement.next
        length += 1
    k = k % length

    lastElement.next = head
    tempNode = head

    for _ in range( length - k - 1 ):
        tempNode = tempNode.next
        
    answer = tempNode.next
    tempNode.next = None
    return answer