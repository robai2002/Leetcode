class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>>v(numRows);
        v[0].push_back(1);
        for(int i=1;i<numRows;i++)
        {
             v[i].push_back(1);
             for(int j=1;j<i;j++)v[i].push_back(v[i-1][j]+v[i-1][j-1]);
             v[i].push_back(1);
        }
        return v;
    }
};