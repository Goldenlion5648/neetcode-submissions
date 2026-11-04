class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        vector<vector<int>> ret;
        for (const auto& interval : intervals) {
            if (ret.empty()) {
                ret.push_back(interval);
                continue;
            }
            int cur_start = interval[0];
            int cur_end = interval[1];
            if (ret.back().back() >= cur_start) {
                ret.back()[1] = max(cur_end, ret.back().back());
            }
            else {
                ret.push_back(interval);
            }
        }
        return ret;
        
    }
};