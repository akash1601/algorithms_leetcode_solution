def threeSumCloset(nums, target):
    nums.sort()
    result = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) -1 
        while j< k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == target:
                return sum
            if abs(sum - target) < abs(result - target):
                result = sum
            if sum < target:
                j  = j + 1
            elif sum > target:
                k = k -1
    return result
threeSumCloset([-1,2,1,-4],1)