def reverse(x):
    num_rev = []
    if x > 0:
        while x > 0:
            num_rev.append(x % 10)
            x = x // 10
        num = int("".join(map(str, num_rev)))
        if num > (2**31-1):
            return 0
        else:
            return num
    elif x < 0:
        x = abs(x)
        while x > 0:
            num_rev.append(x % 10)
            x = x // 10
        num = -(int("".join(map(str, num_rev))))
        if num < (-2**31):
            return 0
        else:
            return num
    else:
        return 0

x = -1534236469
# Output: 321
# x = -123
# Output: -321
# x = 120
# Output: 21
# x = 0
# Output: 0
print(reverse(x))