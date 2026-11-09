class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int og_size = nums.size();
        for (int i = 0; i < og_size; i++) {
            nums.push_back(nums[i]);
        }
        return nums;
    }
};