using LL = long long;
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        erase_if(coins, [&](auto x){
            return x > amount;
        });

        ranges::sort(coins, greater<int>());
        unordered_map<int, int> dp;
        dp[0] = 0;
        for (LL i = 0; i <= amount; i++) {
            if (!dp.contains(i)) {
                continue;
            }
            for (const auto& coin : coins) {
                dp.try_emplace(i+coin, 1e9);                
                if (i + coin <= amount) {
                    dp[i + coin] = min(dp[i] + 1, dp[i + coin]);
                }
            }
        }
        if (!dp.contains(amount)) {
            return -1;
        }
        return dp[amount];
    }
};
