# def removeDuplicates(nums):
#     temp = set(nums)
#     temp = sorted(temp)
#     for idx, elem in enumerate(temp):
#         nums[idx] = elem
#     return len(temp)

def removeDuplicates(nums):
        if not nums:
            return 0
        idx = 0
        for elem in nums:
            if elem != nums[idx]:
                idx+=1
                nums[idx] = elem
        return idx+1

# nums = [0,0,1,1,1,2,2,3,3,4]
nums = [-1,0,0,0,0,3,3]
print(removeDuplicates(nums), " ", nums)