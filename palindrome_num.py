def isPalindrome(x):
    num_list = []
    if x < 0:
        return False
    elif x < (2**31 - 1):
        while x > 0:
            num_list.append(x % 10)
            x = x // 10
        if num_list == num_list[::-1]:
            return True
        else:
            return False

# x = 121
# Output: true
# x = -121
# Output: false
# x = 10
# Output: false
# x = -101
# Output: false
x = 0
# Output: true

print(isPalindrome(x))