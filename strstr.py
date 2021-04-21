# def strStr(haystack, needle):
#     if needle == "":
#         return 0
#     return haystack.find(needle)

def strStr(haystack, needle):
    if needle == "":
        return 0
    
    h_len = len(haystack)
    n_len = len(needle)
    
    for i in range(h_len - n_len + 1):
        if haystack[i:i+n_len] == needle:
            return i
    
    return -1

# haystack = "hello"
# needle = "lo"
# Output: 2
haystack = "aaaaa"
needle = "bba"
# Output: -1
# haystack = ""
# needle = ""
# Output: 0
print(strStr(haystack, needle))