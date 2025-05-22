class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n=nums.size();
        map<int,int>m;
        for(int i=0;i<n;i++)
        {
          if(m[target-nums[i]])return {m[target-nums[i]]-1,i};
          m[nums[i]]=i+1;
        }
        return { };
    }
};