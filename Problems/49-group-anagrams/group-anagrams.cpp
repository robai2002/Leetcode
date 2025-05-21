class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string,vector<string>>m;
        string ind;
        for(auto i:strs)
        {
            ind= i;
            sort(ind.begin(),ind.end());
            m[ind].push_back(i);
        }
        vector<vector<string>>v;
        for(auto i:m)v.push_back(i.second);
        return v;

        
    }
};