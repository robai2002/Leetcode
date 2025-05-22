class Solution {
public:
   int dp(int i,int j,int n,int m,vector<vector<int>>&v)
   {
         if(i==n-1 &&j==m-1)return 1;
         if(i>=n ||j>=m)return 0;
         if(v[i][j]>0)return v[i][j];
          return v[i][j]=dp(i+1,j,n,m,v)+dp(i,j+1,n,m,v);
   }


    int uniquePaths(int n, int m) {
        vector<vector<int>>v(n,vector<int>(m,0));
        return dp(0,0,n,m,v);
    }
};