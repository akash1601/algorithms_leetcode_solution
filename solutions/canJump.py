class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m = 0
        for i, n in enumerate(nums):
            print(i,n)
            if i > m:
                return False
            m = max(m, i+n)
        return True
                