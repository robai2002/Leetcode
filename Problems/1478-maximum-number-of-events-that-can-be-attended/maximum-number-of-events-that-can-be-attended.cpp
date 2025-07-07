class Solution {
public:
    int maxEvents(vector<vector<int>>& events) {
        sort(events.begin(),events.end());
        priority_queue<int,vector<int>,greater<int>> q;
        int x=1,ans=0;
        for(int i=0;i<events.size();i++)
        {
         
         while(!q.empty() &&x<events[i][0])
         {
             if(x<=q.top())x++,ans++;
             q.pop();
         }
        q.push(events[i][1]);
        x=events[i][0];
        }
        while(!q.empty())
        {
            if(x<=q.top())x++,ans++;
            q.pop();
        }     
        return ans;
    }
};