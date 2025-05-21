class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int>ans;
        int n=matrix.size();
        int m=matrix[0].size();
        for(int i=0;2*i<n &&2*i<m;i++)
        {
            
             for(int j=i;j<m-i;j++)ans.push_back(matrix[i][j]);
          for(int j=i+1;j<n-i-1;j++)ans.push_back(matrix[j][m-i-1]);
           if(2*i!=n-1) for(int j=m-1-i;j>=i;j--)ans.push_back(matrix[n-1-i][j]);
            if(2*i!=m-1) for(int j=n-2-i;j>i;j--)ans.push_back(matrix[j][i]);
        }
        return ans;
    }
};