class Solution {
public:
    int rob(vector<int>& nums) {
        int n=nums.size();
     vector<vector<int>>arr(n+10,vector<int>(2,0));
        arr[0][0]=nums[0];
        for(int i=1;i<n;i++)
        {
            arr[i][0]=max(arr[i-1][1]+nums[i],arr[i-1][0]);
            arr[i][1]=max(arr[i-1][1],arr[i-1][0]);
        }
        return arr[n-1][0];

    }
};