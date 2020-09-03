class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ''''lst = set()
        for i in nums1:
            if i in nums2:
                lst.add(i)
        return set(lst)'''
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)