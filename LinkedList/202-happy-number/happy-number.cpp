class Solution {
public:
    bool isHappy(int n) {
        vector<int> num;
        int sum=0;
        while(sum!=1){
            sum=0;
            while(n>0){
                int a=n%10;
                sum+=(a*a);
                n/=10;
            }
            if(find(num.begin(),num.end(),sum)!=num.end())
                return false;
            num.push_back(sum);
            n=sum;
        }
        return true;
    }

};