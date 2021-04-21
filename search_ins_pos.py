def searchInsert(nums, target):
    for idx, elem in enumerate(nums):
        if elem == target:
            return idx
        elif elem > target:
            return idx
    return len(nums)

# nums = [1,3,5,6]
# target = 5
# Output: 2
# nums = [1,3,5,6]
# target = 2
# Output: 1
# nums = [1,3,5,6]
# target = 7
# Output: 4
# nums = [1,3,5,6]
# target = 0
# Output: 0
# nums = [1]
# target = 0
# Output: 0
nums = [1,3,5]
target = 4
# Output: 2

print(searchInsert(nums, target))