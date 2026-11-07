class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        const string VOWELS = "aeuio";
        vector<int> prefix;
        prefix.reserve(words.size() + 1);
        prefix.push_back(0);
        for (const auto& word : words) {
            prefix.push_back(
                prefix.back() +
                int(VOWELS.contains(word.front()) && 
                    VOWELS.contains(word.back())
                )
            );
        }
        
        vector<int> ret;
        ret.reserve(queries.size());
        for (const auto& range : queries) {
            auto start = range[0];
            auto end = range[1];
            ret.push_back(prefix[end + 1] - prefix[start]);
        }
        return ret;
    }
};









