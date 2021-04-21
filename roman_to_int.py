# def romanToInt(s):
#     roman_nums = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
#     if type(s) == str and 1 <= len(s) <= 15:
#         num_list = []
#         num_list_int = []
#         for elem in s:
#             if elem not in roman_nums:
#                 return None
#             else:
#                 num_list.append(elem)
#         for idx in range(len(num_list)):
#             if num_list[idx] == 'I':
#                 if (idx + 1) >= len(num_list):
#                     num_list_int.append(1)
#                 elif num_list[idx+1] == 'V':
#                     num_list_int.append(4)
#                     num_list[idx+1] = 'A'
#                 elif num_list[idx+1] == 'X':
#                     num_list_int.append(9)
#                     num_list[idx+1] = 'A'
#                 else:
#                     num_list_int.append(1)
#             elif num_list[idx] == 'X':
#                 if (idx + 1) >= len(num_list):
#                     num_list_int.append(10)
#                 elif num_list[idx+1] == 'L':
#                     num_list_int.append(40)
#                     num_list[idx+1] = 'A'
#                 elif num_list[idx+1] == 'C':
#                     num_list_int.append(90)
#                     num_list[idx+1] = 'A'
#                 else:
#                     num_list_int.append(10)
#             elif num_list[idx] == 'C':
#                 if (idx + 1) >= len(num_list):
#                     num_list_int.append(100)
#                 elif num_list[idx+1] == 'D':
#                     num_list_int.append(400)
#                     num_list[idx+1] = 'A'
#                 elif num_list[idx+1] == 'M':
#                     num_list_int.append(900)
#                     num_list[idx+1] = 'A'
#                 else:
#                     num_list_int.append(100)
#             elif num_list[idx] == 'V':
#                 num_list_int.append(5)
#             elif num_list[idx] == 'L':
#                 num_list_int.append(50)
#             elif num_list[idx] == 'D':
#                 num_list_int.append(500)
#             elif num_list[idx] == 'M':
#                 num_list_int.append(1000)
#             elif num_list[idx] == 'A':
#                 continue
#         result = 0
#         for elem in num_list_int:
#             result = result + elem       
#         return result
#     else:
#         return None
def romanToInt(s):
        roman_nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        int_nums = [roman_nums[elem] for elem in s]
        for idx in range(1, len(int_nums)):
            if (int_nums[idx-1] < int_nums[idx]):
                    int_nums[idx-1] = - int_nums[idx-1]
        total = sum(int_nums)
        return total

x = "MCMXCIV"
print(romanToInt(x))