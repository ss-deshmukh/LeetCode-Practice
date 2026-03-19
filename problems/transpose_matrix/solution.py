class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)      # rows
        n = len(matrix[0])   # columns

        # Create new matrix with swapped dimensions
        result = [[0] * m for _ in range(n)]

        # Fill transposed values
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]

        return result