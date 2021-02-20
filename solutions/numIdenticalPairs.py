class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        dict = {}
        for num in nums:
            if num in dict:
                counter += dict[num]
                dict[num] += 1
            else:
                dict[num] = 1
        return counter