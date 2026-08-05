class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        d = {}
        for i in range(len(a)):
            d[a[i]] = d.get(a[i],0)+1
            
        for i in range(len(b)):
            if (b[i] not in d or d[b[i]] == 0):
                return False
            else:
                d[b[i]] -=1
                
        return True
    
    
    
    


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna