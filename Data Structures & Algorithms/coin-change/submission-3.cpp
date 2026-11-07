using LL = long long;
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        erase_if(coins, [&](auto x){
            return x > amount;
        });

        ranges::sort(coins, greater<int>());
        vector<int> dp(amount+1, 1e9);
        dp[0] = 0;
        for (LL i = 0; i < dp.size(); i++) {
            if (dp[i] == 1e9) {
                continue;
            }
            for (const auto& coin : coins) {
                if (i + coin < static_cast<LL>(dp.size())) {
                    dp[i + coin] = min(dp[i] + 1, dp[i + coin]);
                }
            }
        }
        if (dp[amount] == 1e9) {
            return -1;
        }
        return dp[amount];
    }
};
