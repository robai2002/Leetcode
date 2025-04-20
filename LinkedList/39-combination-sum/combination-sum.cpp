class Solution {
public:
    void solve(vector<int>& candidates, int target, int ind, vector<vector<int>>& ans, vector<int>& output){
        //base case
        if(target == 0){
            ans.push_back(output);
            return;
        }
        if(target < 0){
            return;
        }

        //recursive relation
        for(int i=ind; i<candidates.size(); i++){
            output.push_back(candidates[i]);
            solve(candidates, target-candidates[i], i, ans, output);
            output.pop_back();
        }
    }


    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> ans;
        vector<int> output;
        int ind = 0;
        solve(candidates, target, ind, ans, output);
        return ans;
    }
};