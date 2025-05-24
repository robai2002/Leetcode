#include <bits/stdc++.h>
using namespace std;
class Solution
{
public:
    set<long long> getsubstr(string &s)
    {
        set<long long> result;
        long long n = s.size();
        for (int len = 1; len <= n; ++len)
        {
            for (int i = 0; i + len <= n; ++i)
            {
                string sub = s.substr(i, len);
                result.insert(stoll(sub));
            }
        }
        return result;
    }
    bool is_prime(long long n){
        for(long long i=2; i*i<=n; i++){
            if(n%i==0) return false;
        }
        return true;
    }
    long long sumOfLargestPrimes(string s)
    {
        set<long long>v=getsubstr(s);
        vector<long long>primes;
        for(auto u:v){
            if(is_prime(u) && u!=1) primes.push_back(u);
        }
        sort(primes.rbegin(),primes.rend());
        long long ans=0;
        for(int i=0; i<=min((int)primes.size()-1,2); i++){
            ans+=primes[i];
        }
        return ans;
    }
};