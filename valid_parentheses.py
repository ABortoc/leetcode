def isValid(s):
    paren_stack = []
    paren_dict = {'}':'{', ']':'[', ')':'('}
    
    for elem in s:
        if elem not in paren_dict:
            paren_stack.append(elem)
        elif paren_stack and paren_dict[elem] == paren_stack[-1]:
            paren_stack.pop(-1)
        else:
            return False
    return paren_stack == []

# Example 1:
# Input: s = "()"
# Output: true
# Example 2:
# Input: s = "()[]{}"
# Output: true
# Example 3:
# Input: s = "(]"
# Output: false
# Example 4:
# Input: s = "([)]"
# Output: false
# Example 5:
# Input: s = "{[]}"
# Output: true
# s = "(){}}{"
# s = "(([]){})"

s = "()[]{}"
print(isValid(s))