class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #number of rows
        n = len(matrix[0]) #number of columns
        L = 0
        R = m * n - 1
        
        while L <= R:
            mid = (L + R) // 2
            mid_row = mid // n
            mid_col = mid % n #after the division by n, it gives the remainder (the position within the row

            if matrix[mid_row][mid_col] < target:
                L = mid + 1
            elif matrix[mid_row][mid_col] > target:
                R = mid - 1
            else:
                return True

        return False 
        