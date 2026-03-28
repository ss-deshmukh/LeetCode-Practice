class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        var_dict = dict()

        for i, e in enumerate(nums):
            if e not in var_dict:
                if target - e in var_dict:
                    return [var_dict[target - e], i]
                else:
                    var_dict[e] = i
            else:
                if e == target - e:
                    return [var_dict[e], i]

        return []

