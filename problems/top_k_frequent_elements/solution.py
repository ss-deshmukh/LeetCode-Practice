class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        output = [[num, count] for num, count in counts.items()]
        output.sort(key=lambda x: x[1], reverse=True)
        return list(output[i][0] for i in range(k))