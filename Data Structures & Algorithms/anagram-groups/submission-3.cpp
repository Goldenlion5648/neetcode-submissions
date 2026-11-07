class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ret;
        unordered_map<string, vector<string>> buckets;

        for (const auto& word : strs) {
            vector<int> counts(26);
            for (const auto& letter : word) {
                counts[letter - 'a'] += 1;
            }
            string key;
            for (int i = 0; i < counts.size(); i++) {
                key += to_string(counts[i]) + ",";
            }
            buckets[key].push_back(word);
        }
        for (const auto& [key, value] : buckets) {
            ret.push_back(move(value));
        }
        return ret;
    }
};
