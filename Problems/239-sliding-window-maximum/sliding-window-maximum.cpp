class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
       vector<int>ans;
       multiset<int,greater<int>>s(nums.begin(),nums.begin()+k-1);
       for(int i=0;i<=nums.size()-k;i++)
       {
          s.insert(nums[i+k-1]);
          ans.push_back(*s.begin());
          s.erase(s.find(nums[i]));
       }
       return ans;
    }
};