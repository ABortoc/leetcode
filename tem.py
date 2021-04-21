class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
l3 = ListNode(1, ListNode(2, ListNode(3)))

while l3:
    print(l3.val)
    l3 = l3.next