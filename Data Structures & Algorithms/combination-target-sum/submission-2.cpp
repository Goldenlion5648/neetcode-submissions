class Solution {
vector<vector<int>> ret;
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        vector<int> so_far;
        so_far.reserve(60);
        search(target, 0, 0, so_far, nums);
        return ret;
    }

    void search(int goal, int total, int nums_index, vector<int>& current, vector<int>& nums) {
        if (total == goal) {
            ret.push_back(current);
            return;
        }
        if (total > goal || nums_index >= nums.size()) {
            return;
        }

        while (nums_index < nums.size())
        {
            current.push_back(nums.at(nums_index));
            search(goal, total + nums.at(nums_index), nums_index, current, nums);
            current.pop_back();
            nums_index += 1;
        }
    }
    
};
