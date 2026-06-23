# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return []

        def traversal(node, emptylist):
            if not node:
                return []
            traversal(node.left, emptylist)
            emptylist.append(node.val)
            traversal(node.right, emptylist)

        traversal(root, result)
        return result