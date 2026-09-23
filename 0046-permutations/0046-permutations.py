class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(current):
            if len(current) == len(nums):
                result.append(current.copy())
                return

            for num in nums:
                if num not in current:
                    current.append(num)

                    backtrack(current)

                    current.pop()

        backtrack([])

        return result
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna