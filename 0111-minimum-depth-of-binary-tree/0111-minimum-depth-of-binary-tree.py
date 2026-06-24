class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)

        if root.left and not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.right), self.minDepth(root.left))
