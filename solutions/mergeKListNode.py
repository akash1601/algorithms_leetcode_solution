def mergeKListNode(nums):
    if not nums:
        return
    if len(nums) == 1:
        return nums[0]
    mid = len(nums) // 2
    l = mergeKListNode(nums[:mid])
    r = mergeKListNode(nums[mid:])
    return mergeList(l,r)
    
def mergrList(l,r):
    curr = a = ListNode(0)
    while l1 and l2:
        if l.val < = r.val:
            curr.next = ListNode(l.val)
            l = l.next
        else:
            curr.next = ListNode(r.val)
            r = r.next
        curr = curr.next
    curr.next = l1 or l2
    return a.next