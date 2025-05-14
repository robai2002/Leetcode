class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min=INT_MAX;
        int max=0;
        int pp=0;
        for(int i=0;i<prices.size();i++)
        {
            if(prices[i]<min)
            {
                min=prices[i];
            }
            pp=prices[i]-min;
            if(max<pp)
            {
                max=pp;
            }
        }
        return max;
    }
};