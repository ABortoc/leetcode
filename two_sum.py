def twoSum(nums, target):
    for i in range(len(nums)):
        for k in range(i+1, len(nums)):
            if nums[i] + nums[k] == target:
                return i, k


# def twoSum(nums, target):
#     hash_map = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement not in hash_map:
#             hash_map[num] = i
#         else:
#             return [hash_map[complement], i]

nums = [2,5,5,11]
target = 10
# nums = [3,2,4]
# target = 6
# nums = [3,3]
# target = 6
# nums = [2,7,11,15]
# target = 9
print(twoSum(nums, target))