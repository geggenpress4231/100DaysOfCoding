#check columns and then go for rows



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        cols = len(matrix[0])
        left, right = 0, len(matrix) - 1

        
        while left <= right:
            row = (left + right) // 2
            if matrix[row][-1] < target:
                left = row + 1
            elif matrix[row][0] > target:
                right = row - 1
            else:
                break 

        if not (left <= right):
            return False

        row = (left + right) // 2
        l, r = 0, cols - 1

       
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True

        return False



