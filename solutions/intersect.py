class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = Counter()
        res = []
        if len(nums2)<len(nums1):
            nums1, nums2 = nums2, nums1
        for num in nums1:
            dict1[num]+=1
       
        for num in nums2:
            if num in dict1 and dict1[num]!=0:
                dict1[num]-=1
                res.append(num)
            #print (dict1)
        return res
        