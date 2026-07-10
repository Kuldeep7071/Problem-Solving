class Solution {
public:
     bool isPerfectSquare(int num) {
        int high = 1, low = num;
        while (high <= low) {
            int mid = high + (low - high) / 2; // Avoids overflow
            long square = (long)mid * mid; // Cast to long to prevent overflow
            if (square == num)
                return true;
            else if (square < num)
                high = mid + 1;
            else
                low = mid - 1;
        }
        return false;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna