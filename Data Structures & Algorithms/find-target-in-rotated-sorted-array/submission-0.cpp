class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto pos = std::find(nums.begin(), nums.end(), target);
        if (pos == nums.end()) {
            return -1;
        }
        return pos - nums.begin();
    }
};
