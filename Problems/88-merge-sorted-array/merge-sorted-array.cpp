class Solution {
public:
   void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        n-=1,m-=1;
        int x;
        for(int i=n+m+1;i>=0;i--)
        {
            if(n<0)break;
         x=(m>=0)?nums1[m]:nums2[n];
         if(x<=nums2[n])x=nums2[n],n--;
         else m--;
         nums1[i]=x;
        }
        return ;
    }
};