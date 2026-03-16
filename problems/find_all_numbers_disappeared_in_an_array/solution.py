class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_map = dict()
        result = list()

        for i in range(len(nums)):
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
            else:
                hash_map[nums[i]] = 1

        for i in range(1,len(nums)+1):
            if i not in hash_map:
                result.append(i)

        return result