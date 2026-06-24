class Solution:
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def dfs(node):
            nonlocal diameter

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # longest path through this node
            diameter = max(diameter, left + right)

            # return height
            return 1 + max(left, right)
            
        dfs(root)
        return diameter