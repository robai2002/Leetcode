class Solution {
public:
    int climbStairs(int n) {
        int a[n+1];
        a[0]=a[1]=1;
        for(int i=2;i<=n;i++)a[i]=a[i-1]+a[i-2];
        return a[n];
    }
};