class Solution {
public:
    void nextPermutation(vector<int>& nums) {
       int n=nums.size()-1;
       int infpt=0;
       for(int i=n;i;i--)
       {
           if(nums[i]>nums[i-1])
           {
               infpt=i;
                break;
    
           }
       } 
       if(infpt==0)
       {
 sort(nums.begin(),nums.end());
          return ;
       }
       int x=infpt;
       for(int i=infpt;i<=n;i++)
       {
           if(nums[infpt-1]<nums[i] &&nums[i]<nums[x])x=i;
       }

       swap(nums[x],nums[infpt-1]);
       sort(nums.begin()+infpt,nums.end());
       return ;
       
    }
};