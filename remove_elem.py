def removeElement(nums, val):
    counter = 0
    counter_i = 0
    for idx, elem in enumerate(nums):
        if elem == val:
            temp = nums[counter_i]
            nums[counter_i] = nums[idx]
            nums[idx] = temp
            counter += 1
            counter_i += 1
    nums.reverse()
    return len(nums) - counter

nums = [3,2,2,3]
# nums = [0,1,2,2,3,0,4,2]
print(removeElement(nums, 3), " ", nums)