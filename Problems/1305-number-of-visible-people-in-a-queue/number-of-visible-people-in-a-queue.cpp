typedef long long ll;
class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        vector<int>ans;
        stack<ll>s;
        
        int cnt=0;
        for(int i=heights.size()-1;~i;i--)
        {
            cnt = 0;
            while(!s.empty() && s.top()<heights[i]){
                cnt++;
                s.pop();
            }
            if(!s.empty())cnt++;
            ans.push_back(cnt);
            s.push(heights[i]);
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};