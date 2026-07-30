class Solution:
    def countDigits(self, n):
        # code here
        count=0
        while(n>0):
            count+=1
            n=n//10
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna