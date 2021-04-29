"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    def traverse(p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        if p.val != q.val:
            return False
        return traverse(p.left, q.left) and traverse(p.right, q.right)
    return traverse(p, q)

# p = TreeNode(1, TreeNode(2), TreeNode(3))
# q = TreeNode(1, TreeNode(2), TreeNode(3))
# p = TreeNode(1, TreeNode(2), None)
# q = TreeNode(1, None, TreeNode(2))
# p = TreeNode()
# q = TreeNode(1)
p = TreeNode(10, TreeNode(5), TreeNode(15)) #[10,5,15]
q = TreeNode(10, TreeNode(5, None, 15), None) #[10,5,null,null,15]
print(isSameTree(p, q))