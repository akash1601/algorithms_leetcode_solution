def swapNodes(lists):
    pre.next = head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next = b
        b.next = a
        a.next = b.next