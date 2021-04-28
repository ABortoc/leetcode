"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
Constraints:
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def deleteDuplicates(head):
#     if head:
#         head_temp = ListNode()
#         clean_list = head_temp
#         temp = -101
#         while head:
#             if head.next:
#                 if head.val != temp:
#                     temp = head.val
#                     head_temp.val = temp
#                     head = head.next
#                     if head.val == temp:
#                         continue
#                     else:
#                         head_temp.next = ListNode()
#                         head_temp = head_temp.next
#                 else:
#                     head = head.next
#                     if head.val != temp:
#                         head_temp.next = ListNode()
#                         head_temp = head_temp.next
#             else:
#                 if head.val != temp:
#                     temp = head.val
#                     head_temp.val = head.val
#                     head = head.next
#                 else:
#                     head = head.next
#         return clean_list
#     else:
#         return head

def deleteDuplicates(head):
    if not head:
        return head
    llist_a = ListNode()
    llist_a = head
    llist_a = head.next
    llist_b = ListNode()
    llist_b = head
    while llist_a:
        if llist_a.val == llist_b.val:
            llist_b.next = llist_a.next
            llist_a = llist_a.next
        else:
            llist_b = llist_b.next
            llist_a = llist_a.next
    return head

#l1 = ListNode(1, (ListNode(1, ListNode(2, ListNode(3, ListNode(3))))))
#l1 = ListNode(1, (ListNode(1, ListNode(2))))
l1 = ListNode(1, (ListNode(1, ListNode(1))))
l2 = deleteDuplicates(l1)
while l2:
    print(l2.val)
    l2 = l2.next