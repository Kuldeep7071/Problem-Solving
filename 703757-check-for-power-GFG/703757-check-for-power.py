class Solution:
    def isPower(self, x, y):
        if y == 1:
            return True

        if x == 1:
            return y == 1

        while y % x == 0:
            y //= x

        return y == 1
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna