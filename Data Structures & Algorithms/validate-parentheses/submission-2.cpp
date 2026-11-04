class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for (const auto& letter : s) {
            if (stack.empty()) {
                stack.push_back(letter);
                continue;
            }
            unordered_map<char, char> close_to_open = {
                {')', '('},
                {']', '['},
                {'}', '{'},
            };
            if (string("[{(").find(letter) != string::npos) {
                stack.push_back(letter);
            } else {
                if (stack.empty()) {
                    return false;
                }
                if (close_to_open[letter] != stack.back()) {
                    return false;
                }
                stack.pop_back();
            }
        }
        return stack.empty();
    }
};
