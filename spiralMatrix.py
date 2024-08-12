class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        if (matrix.empty()) return res;

        int top = 0, bottom = matrix.size() - 1;
        int left = 0, right = matrix[0].size() - 1;

        while (top <= bottom && left <= right) {
            // Traverse from left to right
            for (int j = left; j <= right; ++j) {
                res.push_back(matrix[top][j]);
            }
            top++;

            // Traverse from top to bottom
            for (int i = top; i <= bottom; ++i) {
                res.push_back(matrix[i][right]);
            }
            right--;

            // Traverse from right to left, if any row remains
            if (top <= bottom) {
                for (int j = right; j >= left; --j) {
                    res.push_back(matrix[bottom][j]);
                }
                bottom--;
            }

            // Traverse from bottom to top, if any column remains
            if (left <= right) {
                for (int i = bottom; i >= top; --i) {
                    res.push_back(matrix[i][left]);
                }
                left++;
            }
        }

        return res;
    }
};

