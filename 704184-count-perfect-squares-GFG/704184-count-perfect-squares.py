class Solution:
    def countSquares(self, n):
        # code here 
        if n <= 1:
            return 0
        i = 1
        while i * i < n:
            i += 1
        return i - 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna