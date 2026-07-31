class Solution:
    def reverseArray(self, arr):
        # code here
        left =0
        right = len(arr)-1
        
        while(left<right):
            arr[left],arr[right]= arr[right],arr[left]
            left+=1
            right-=1
            
        return arr
        
        
        #or we can also use built in method like- 
        #arr[::-1]
        #arr.reverse()

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna