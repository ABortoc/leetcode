"""
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.
A word is a maximal substring consisting of non-space characters only.
Example 1:
Input: s = "Hello World"
Output: 5
Example 2:
Input: s = " "
Output: 0
"""
def lengthOfLastWord(s):
    if not s or s == " " or s.isspace():
        return 0
    s.rstrip()
    word_list = s.split()
    return len(word_list[-1])

s = "        "
print(lengthOfLastWord(s))