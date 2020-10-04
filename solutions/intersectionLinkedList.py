class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(headA: ListNode, headB: ListNode):
        p, q = headA, headB;
        while p != q:
            if p:
                p = p.next 
            else:
                p = headB
            if q:
                q = q.next 
            else:
                q = headA
            
        return p;