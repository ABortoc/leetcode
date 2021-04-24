"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Example 3:
Input: digits = [0]
Output: [1]
"""
# def plusOne(digits):
#     remainder = False
#     if digits[-1] != 9:
#         digits[-1] += 1
#         return digits
#     elif len(digits) == 1 and digits[0] == 9:
#         digits[0] = 0
#         digits.insert(0, 1)
#         return digits
#     else:
#         for idx, elem in reversed(list(enumerate(digits))):
#             if elem != 9 and remainder == True:
#                 digits[idx] += 1
#                 remainder = False
#                 return digits
#             elif elem == 9 and idx != 0:
#                 digits[idx] = 0
#                 remainder = True
#             elif elem == 9 and idx == 0 and remainder == True:
#                 digits[idx] = 0
#                 digits.insert(0, 1)
#                 remainder = False
#         return digits

# def plusOne(digits):
#     list_to_num = ''.join(str(digits).lstrip('[').rstrip(']').split(', '))
#     return [elem for elem in str(int(list_to_num)+1)]

def plusOne(digits):
    for i in range(len(digits))[::-1]:
        digits[i] += 1
        if digits[i] != 10: return digits
        digits[i] = 0
    return [1] + digits

# digits = [9, 8, 7, 6, 9]
# digits = [9,8,9]
# digits = [4,3,2,9]
# digits = [1,9,9]
# digits = [9, 9, 9]
# digits = [9]
digits = [2,4,9,3,9]
print(plusOne(digits))