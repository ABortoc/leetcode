"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Example 1:
Input: x = 4
Output: 2
Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""
from math import sqrt

def mySqrt(x):
    if x == 0 or x == 1:
        return x
    
    start = 1
    end = x
    
    while(start <= end):
        mid = (start + end) // 2
        if(mid*mid == x):
            return mid
        if(mid*mid < x):
            start = mid + 1
            result = mid
        else:
            end = mid - 1
        
    return result

x = 4
print(mySqrt(48))