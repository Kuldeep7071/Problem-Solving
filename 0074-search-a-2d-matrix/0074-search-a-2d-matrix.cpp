class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int row = matrix.size();
        int col = matrix[0].size();
    
        int left = 0, right = row * col - 1;
    
        while (left <= right) {
           int mid = left + (right - left) / 2;
           int mid_value = matrix[mid/col][mid%col]; 
           if (mid_value == target) {
            return true; 
            } 
            else if (mid_value < target) {
                left = mid + 1; 
            } 
            else {
                right = mid - 1; 
            }
        }
    
        return false; 
    }

};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna