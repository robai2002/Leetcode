class Solution {
public:
   bool isIsomorphic(string s, string t) {
        vector<int>v(300,-1);
        vector<int>v1(300,-1);
        for(int i=0;i<s.size();i++)
        {
         if(v[s[i]]==-1 &&v1[t[i]]==-1)v[s[i]]=t[i],v1[t[i]]=s[i];
         else if(v[s[i]]!=t[i] || v1[t[i]]!=s[i])return false;
        }
        return true;
    }
};