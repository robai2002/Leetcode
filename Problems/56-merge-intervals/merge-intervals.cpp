class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& a) {
        map<int,int>m;
        vector<vector<int>>output;
        for (auto i:a)
        {
            m[i[0]]++,m[i[1]]--;
        }
        int x = 0,y = -1;
        for (auto i:m)
        {
           if ( x==0 &&y<0)y =i.first;
           x+=i.second;
           if(x==0 &&y>=0)
           output.push_back({y, i.first}),y =-1;
        }
        return output;
    }
};