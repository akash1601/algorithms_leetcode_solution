class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        def feasible(threshold) -> bool:
            count = 1
            total = 0
            for num in nums:
                total = total + num
                if total > threshold:
                    total = num
                    count += 1
                    
                    if count > m:
                        return False
            return True
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left