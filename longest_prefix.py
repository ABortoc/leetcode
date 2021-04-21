# def longestCommonPrefix(strs):
#     if strs:
#         for elem in strs:
#             if elem == '':
#                 return ''
#         prefix = ''
#         strs.sort(key=len)
#         letters = [letter for letter in strs[0]]
#         idx = 0
#         exists = True
#         while idx < len(strs[0]):
#             for elem in strs:
#                 if elem[idx] == letters[idx]:
#                     continue
#                 else:
#                     exists = False
#             if exists:
#                 prefix = prefix + letters[idx]
#                 idx = idx + 1
#             else:
#                 break
#         return prefix
#     else:
#         return ''

def longestCommonPrefix(strs):
    if not strs:
        return ''
    strs.sort()
    prefix = []
    for idx, char in enumerate(strs[0]):
        if char == strs[-1][idx]:
            prefix.append(char)
        else:
            break
    return ''.join(prefix)
        

# strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs = ['ab', 'a']
# strs = ["flower","flower","flower","flower"]
strs = ["abab","aba","abc"]

print(longestCommonPrefix(strs))

'''
given a list of words take the fist letter of the fist word and check
if all other words contain it in the same position...
break each word into a list of letters and compare each list by position
'''