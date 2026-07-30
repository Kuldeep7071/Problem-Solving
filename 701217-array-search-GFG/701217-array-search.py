class Solution:
    def search(self, arr, x):
        # code here
        for i in range (len(arr)):
            if arr[i] == x:
                return i
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna