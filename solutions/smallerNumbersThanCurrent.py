class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        dict = {}
        ans = []
        for i in range(len(nums)):
            if temp[i] not in dict:
                dict[temp[i]] = i
        for i in range(len(nums)):
            ans.append(dict[nums[i]])
        return ans
                