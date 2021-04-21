class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1, l2):
    head = ListNode()
    l3 = head       
    while l1 or l2:
        if l1 and l2:
            if l1.val<=l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2=l2.next
        elif l1 and not l2:
            head.next = l1
            break
        else:
            head.next = l2
            break
        
        head = head.next
    
    return l3.next

# Example 1:
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:
# Input: l1 = [], l2 = []
# Output: []
# Example 3:
# Input: l1 = [], l2 = [0]
# Output: [0]