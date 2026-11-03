class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> val_to_pos;
        int i = 0;
        for (const auto& num : nums) {
            if (val_to_pos.contains(target - num)) {
                vector<int> ret = {val_to_pos[target - num], i};
                return ret;
            }
            val_to_pos[num] = i;
            i += 1;

        }
    }
};
