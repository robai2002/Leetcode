class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int,int>m;
        for(int i=1;i<=nums.size();i++)
        {
            if(m[nums[i-1]] &&i-m[nums[i-1]]<=k)return true;
            m[nums[i-1]]=i;
        }
        return false;
    }
};