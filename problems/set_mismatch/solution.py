class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}
        duplicate = 0

        # Count occurrences
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] == 2:
                duplicate = num

        # Find missing by checking which number from 1 to n is not in count
        n = len(nums)
        for i in range(1, n + 1):
            if i not in count:
                return [duplicate, i]