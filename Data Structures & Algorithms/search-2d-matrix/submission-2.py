class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        HEIGHT = len(matrix)
        WIDTH = len(matrix[0])

        left, right = 0, HEIGHT * WIDTH - 1

        while left <= right:
            mid1 = (left + right) // 2
            matrix_value = matrix[mid1 // WIDTH][mid1 % WIDTH] 
            if target == matrix_value:
                return True
            elif target > matrix_value:
                left = mid1 + 1
            else:
                right = mid1 - 1
        return False