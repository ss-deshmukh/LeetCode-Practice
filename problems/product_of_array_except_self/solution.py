class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefix_prod = 1
        suffix_prod = 1
        
        for i in range(n):

            res[i] *= prefix_prod
            prefix_prod *= nums[i]

            j = n - 1 - i
            res[j] *= suffix_prod
            suffix_prod *= nums[j]
            
        return res