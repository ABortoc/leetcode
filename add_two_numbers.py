"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1list, l2list = [], []
        temp = ListNode()
        l3 = temp
        while l1:
            l1list.append(l1.val)
            l1 = l1.next
        while l2:
            l2list.append(l2.val)
            l2 = l2.next
        result = int("".join(map(str, l1list[::-1]))) + int("".join(map(str, l2list[::-1])))
        while result > 0:
            temp.val = result % 10
            result = result // 10
            if result != 0:
                temp.next = ListNode()
                temp = temp.next
        return l3
    
# l1 = ListNode(2, (ListNode(4, ListNode(3))))
# l2 = ListNode(5, (ListNode(6, ListNode(4))))
# l1 = ListNode(9, (ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))))
# l2 = ListNode(9, (ListNode(9, ListNode(9, ListNode(9)))))
# l1 = ListNode()
# l2 = ListNode()
l1 = ListNode(2, (ListNode(4, ListNode(9))))
l2 = ListNode(5, (ListNode(6, ListNode(4, ListNode(9)))))

obj = Solution()
l3 = obj.addTwoNumbers(l1, l2)
while l3:
    print(l3.val)
    l3 = l3.next