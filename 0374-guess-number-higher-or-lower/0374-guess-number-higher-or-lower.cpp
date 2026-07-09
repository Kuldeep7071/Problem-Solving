/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int left = 1, right = n;                 // search interval [left, right]

        while (left <= right) {
            // Prevent overflow for very large `n`
            int mid = left + (right - left) / 2;

            int res = guess(mid);                // call the provided API

            if (res == 0)                        // found the number
                return mid;
            else if (res == -1)                  // hidden number is smaller
                right = mid - 1;
            else                                 // res == 1, hidden number is larger
                left = mid + 1;
        }

        // The problem guarantees a solution exists, so we never reach here.
        return -1;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna