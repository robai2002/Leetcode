class Solution {
public:
    int res = INT_MAX;
    int n, sessionTime;
    
    void dfs(int idx, vector<int>& tasks, vector<int>& sessions, int used) {
        if (used >= res) return; 
        if (idx == n) {
            res = used;
            return;
        }

        for (int i = 0; i < used; ++i) {
            if (sessions[i] + tasks[idx] <= sessionTime) {
                sessions[i] += tasks[idx];
                dfs(idx + 1, tasks, sessions, used);
                sessions[i] -= tasks[idx]; 
            }
        }

        sessions[used] = tasks[idx];
        dfs(idx + 1, tasks, sessions, used + 1);
        sessions[used] = 0; 
    }

    int minSessions(vector<int>& tasks, int sessionTime_) {
        sessionTime = sessionTime_;
        n = tasks.size();

        sort(tasks.rbegin(), tasks.rend()); 
        vector<int> sessions(n, 0); 
        dfs(0, tasks, sessions, 0);
        return res;
    }
};