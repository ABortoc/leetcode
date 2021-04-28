"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
Constraints:
    1 <= n <= 45
"""
# def climbStairs(n):
#     if n <= 0 or n >= 46:
#         return 0
#     elif n == 1:
#         return 1
#     return climbStairs(n - 1) + climbStairs(n - 2)

# def climbStairs(n):
#     if n <= 0 or n >= 46:
#         return 0
#     elif n == 1:
#         return 1
    
#     temp = 0
#     result = [1]
    
#     for idx in range(1, n + 1):
#         stairs = idx - 2 - 1
#         e = idx - 1
#         if(stairs >= 0):
#             temp -= result[stairs]
#         temp += result[e]
#         result.append(temp)
    
#     return result[n]

def climbStairs(n):
    if n <= 1:
        return 1
    result = [0 for i in range(n+1)]
    result[0] = 0
    result[1] = 1
    result[2] = 2
    index = 3
    while index <= n:
        result[index] = result[index-1] + result[index-2]
        index += 1
    return result[index-1]

n = 45
print(climbStairs(n))