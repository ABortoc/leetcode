"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    if not root:
        return True
    queue = [root]
    while queue:
        values = []
        for idx in range(len(queue)):
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                values.append(node.left.val)
            else:
                values.append("null")
            if node.right:
                queue.append(node.right)
                values.append(node.right.val)
            else:
                values.append("null")
        if values != values[::-1]:
            return False
    return True

#p = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
#p = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(3)))
#p = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
p = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(5), TreeNode(6)), TreeNode(4, TreeNode(7), TreeNode(8))), TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(7)), TreeNode(3, TreeNode(6), TreeNode(5))))
print(isSymmetric(p))
