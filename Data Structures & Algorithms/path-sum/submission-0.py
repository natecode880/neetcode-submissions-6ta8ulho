class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def findPath(root, currentSum):
            if not root:
                return False
            
            currentSum += root.val
            
            if not root.left and not root.right:
                return currentSum == targetSum
            
            return findPath(root.left, currentSum) or findPath(root.right, currentSum)
            
        return findPath(root, 0)