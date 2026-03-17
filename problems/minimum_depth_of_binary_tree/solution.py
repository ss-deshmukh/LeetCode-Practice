# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        que = [root]
        depth = 0

        while que:
            depth += 1
            next_que = []

            for node in que:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)

            que = next_que

        return depth