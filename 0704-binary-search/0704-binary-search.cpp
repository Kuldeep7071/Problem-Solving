class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        
        while (l <= r) {
            int mid = (l + r) / 2; // Integer division equivalent to Python's (l+r)//2
            if (target == nums[mid]) {
                return mid;
            } 
            // Search right half
            else if (target > nums[mid]) {
                l = mid + 1;
            } 
            // Search left half
            else {
                r = mid - 1;
            }
        }
        return -1;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna