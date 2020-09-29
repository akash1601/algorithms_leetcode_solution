def isPalindrome(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]