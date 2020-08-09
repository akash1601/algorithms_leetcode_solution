def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - 1):
            if nums[j] > nums[j+1]:
                temp_nums = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp_nums
                
    return nums
bubbleSort([1,1,4,2,2,3])