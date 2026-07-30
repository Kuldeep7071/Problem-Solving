class Solution:
	def countOddEven(self, arr):
		#Code here
		odd = 0
		even = 0
		
		for i in arr:
		    if(i%2==0):
		        even+=1
		    else:
		        odd+=1
        return odd,even
		  

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna