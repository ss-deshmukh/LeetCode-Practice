1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        var_dict = dict()
4
5        for i, e in enumerate(nums):
6            search = target - e
7
8            if search in set(nums[i+1:]):
9                return [i, nums.index(search, i+1)]