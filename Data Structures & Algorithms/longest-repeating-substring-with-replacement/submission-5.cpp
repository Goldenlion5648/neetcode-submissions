class Solution {
public:
    int characterReplacement(const string& s, int k) {
        int left = 0;
        unordered_map<char, int> seen_count;
        int ret = -1;
        int highest_value = 0;
        for (int i = 0; i < s.size(); i++) {
            seen_count[s[i]] += 1;
            highest_value = max(highest_value, seen_count[s[i]]);
            while ((i + 1 - left) - highest_value > k) {
                seen_count[s[left]] -= 1;
                if (seen_count[s[left]] == 0) {
                    seen_count.erase(s[left]);
                }
                left += 1;
            }
            ret = max(ret, i + 1 - left);
        }
        return ret;
    }
};