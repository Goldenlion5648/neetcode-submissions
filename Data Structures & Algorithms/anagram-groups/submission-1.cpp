class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ret;
        unordered_map<string, vector<string>> sorted_to_words; 
        for (const auto& word : strs) {
            string key = word;
            sort(key.begin(), key.end());
            sorted_to_words[key].push_back(word);
        }
        for (auto [key, value] : sorted_to_words) {
            ret.push_back(value);
        }
        return ret;

    }
};
