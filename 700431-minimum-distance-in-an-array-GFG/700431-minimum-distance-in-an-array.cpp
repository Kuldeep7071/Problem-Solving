class Solution {
  public:
    int minDist(vector<int>& arr, int x, int y) {
        // code here
        int n=arr.size();
        int ls = -1;
        int mini =INT_MAX;
        for(int i=0;i<n;i++){
            if(arr[i] == x || arr[i] == y){
                if(ls != -1 && arr[i]!=arr[ls]){
                    int dist= abs(i-ls);
                    mini= min(mini,dist);
                }
                ls=i;
            }
        }
        return (mini == INT_MAX) ? -1 : mini;
    }
};

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna