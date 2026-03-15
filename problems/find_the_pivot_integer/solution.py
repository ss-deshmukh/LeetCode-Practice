class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = (n * (n+1)) / 2
        left = 0
        for i in range(1,n+1):
            left+=i
            if left == sum - left + i:
                return i
        return -1