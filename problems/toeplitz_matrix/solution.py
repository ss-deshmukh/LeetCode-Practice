class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        #if not matrix:
         #   return True

        for r in range(len(matrix)-1):
            for c in range(len(matrix[0])-1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
        return True
