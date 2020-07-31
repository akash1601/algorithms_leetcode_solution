def fourSum(nums, target):
    nums.sort()
    
    length = len(nums) - 1
    result = []
    for i in range(length - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, length-1):
            if j> i+1 and nums[j] == nums[j - 1]:
                continue
            k = j +1
            h = length
            while k < h:
                curr = nums[i] + nums[j] + nums[k] + nums[h]
                if curr == target:
                    result.append([nums[i],nums[j],nums[k],nums[h]])
                    while k < h and nums[k] == nums[k+1]:
                        k = k+1
                    while k < h and nums[h] == nums[h-1]:
                        h = h-1
                    k = k+1
                    h = h-1
                elif curr>target:
                    h = h-1
                else:
                    k = k+1
    print(result)
fourSum([1, 0, -1, 0, -2, 2],0)