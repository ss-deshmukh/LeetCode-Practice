class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # Calculate total sum first
        total_sum = sum(sum(row) for row in grid)
        
        # If the total sum is odd, it's impossible to split into two equal integer parts
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        
        # 1. Check Horizontal Slices (O(1) extra space)
        running_row_sum = 0
        for i in range(m - 1): # Stop at m-1 to ensure non-empty sections
            running_row_sum += sum(grid[i])
            if running_row_sum == target:
                return True
        
        # 2. Check Vertical Slices (O(1) extra space)
        running_col_sum = 0
        for j in range(n - 1): # Stop at n-1 to ensure non-empty sections
            # Sum the current column
            for i in range(m):
                running_col_sum += grid[i][j]
            
            if running_col_sum == target:
                return True
                
        return False