

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Traverse from left to right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Traverse from right to left, if any row remains
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Traverse from bottom to top, if any column remains
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
