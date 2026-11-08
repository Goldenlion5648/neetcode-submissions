class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> seen;
        for (const auto& letter : s) {
            seen[letter] += 1;
        }
        unordered_map<char, int> seen2;
        for (const auto& letter : t) {
            seen[letter] -= 1;
        }
        return all_of(seen.begin(), seen.end(), [&](auto x){
            return seen[x.first] == 0;
        });
        

    }
};
