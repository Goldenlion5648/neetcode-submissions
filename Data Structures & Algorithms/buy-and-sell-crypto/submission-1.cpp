class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lowest = prices[0];
        int ret = 0;
        for (const auto& price: prices) {
            ret = max(ret, price - lowest);
            lowest = min(lowest, price);
        }
        return ret;
    }
};
