from time import perf_counter_ns
start = perf_counter_ns()
# def maxSubArray(nums):
#         max_sum = nums[0]
#         current_sum = 0
		
#         for elem in nums:
#             if current_sum < 0:
#                 current_sum = 0
#             current_sum += elem
#             max_sum = max(max_sum, current_sum)
			
#         return max_sum  
def maxSubArray(nums):
    current_sum = nums[0]
    max_sum = current_sum
    for elem in nums[1:]:
        current_sum = max(current_sum + elem, elem)
        max_sum = max(max_sum, current_sum)
    return max_sum
# def maxSubArray(nums):
#     if not nums:
#         return 0
#     elif len(nums) == 1:
#         return nums[0]
    
#     max_sum = nums[0]
#     temp_sum = nums[0]
    
#     for idx in range(1, len(nums)):
#         temp_sum += nums[idx]
#         if nums[idx] > max_sum and nums[idx-1] < 0 and temp_sum < nums[idx]:
#             max_sum = nums[idx]
#             temp_sum = nums[idx]
#         elif nums[idx] > max_sum and nums[idx-1] >= 0 and temp_sum < nums[idx]:
#             max_sum += nums[idx]
#             temp_sum = max_sum
#         else:
#             if temp_sum > max_sum:
#                  max_sum = temp_sum
#             elif temp_sum < nums[idx]:
#                 temp_sum = nums[idx]
    
#     return max_sum
end = perf_counter_ns()
# Example 1:
nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
# nums = [1]
# Output: 1
# Example 3:
# nums = [5,4,-1,7,8]
# Output: 23
# Example 4:
# nums = [1,2]
# Output: 3
# Example 5:
# nums = [8,-19,5,-4,20]
# Output: 21

print(maxSubArray(nums), " ", end-start)