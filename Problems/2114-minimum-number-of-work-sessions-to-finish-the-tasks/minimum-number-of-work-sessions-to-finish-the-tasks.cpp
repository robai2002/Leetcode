class Solution {
public:
    pair<int, int> get_ans(map<long long int, pair<int, int>>& mp, vector<int>& tasks, int val, const int sessionTime) {
        if (mp.count(val)) return mp[val];
        pair<int, int> best = {1e9, 0};  

        int n = tasks.size();
        for (int i = 0; i < n; i++) {
            if ((val & (1 << i)) == 0) { 
                
                pair<int, int> res = get_ans(mp, tasks, val | (1 << i), sessionTime);

                if (res.second < tasks[i]) {
                    res.first++;
                    res.second = sessionTime - tasks[i];
                } else {
                    res.second -= tasks[i];
                }

                if (res.first < best.first || (res.first == best.first && res.second > best.second)) {
                    best = res;
                }
            }
        }

        if (best.first == 1e9) return {0, 0}; 
        return mp[val] = best;
    }

    int minSessions(vector<int>& tasks, int sessionTime) {
        map<long long int, pair<int, int>> mp;
        int n = tasks.size();
        mp[(1 << n) - 1] = {0, 0}; 
        return get_ans(mp, tasks, 0, sessionTime).first;
    }
};
