class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        # Find the maximum value and its index
        max_val = max(nums)
        max_idx = nums.index(max_val)

        # Split the array
        left = nums[:max_idx]
        right = nums[max_idx + 1:]

        # Create the root node and recursively build left and right subtrees
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)

        return root