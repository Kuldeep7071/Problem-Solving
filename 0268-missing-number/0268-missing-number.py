class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s1=n*(n+1)//2
        s2=0
        for i in nums:
            s2+=i
        return s1-s2
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna