class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for (const auto& elem : nums) {
            counts[elem] += 1;
        }
        std::priority_queue<pair<int, int>, vector<pair<int, int>>, std::greater<pair<int, int>>> largest;
        for (const auto& [elem, count] : counts) {
            largest.push(make_pair(count, elem));
            if (largest.size() > k) {
                largest.pop();
            }
        }
        vector<int> ret;
        while (!largest.empty())
        {
            ret.push_back(largest.top().second);
            largest.pop();
        }
        return ret;
        
    }
};
