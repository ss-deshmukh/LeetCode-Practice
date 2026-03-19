class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        r, d, l, u = (0, 1), (1, 0), (0, -1), (-1, 0)
        dir_ord = {r: d, d: l, l: u, u: r}

        bin = [[0] * n for i in range(m)]
        result = []
        row, col = 0, 0
        dir = r

        while len(result) != (m * n):
            result.append(matrix[row][col])
            bin[row][col] = 1

            # Check if next position is valid
            next_row, next_col = row + dir[0], col + dir[1]
            if (next_row >= m or next_row < 0 or next_col >= n or next_col < 0 or bin[next_row][next_col] == 1):
                dir = dir_ord[dir]
                next_row, next_col = row + dir[0], col + dir[1]

            row, col = next_row, next_col

        return result