class Solution {
public:
    bool isPalindrome(string s) {
        string filtered = "";
        for (const auto& letter : s) {
            if (std::isalpha(letter) || std::isdigit(letter)) {
                filtered.push_back(std::tolower(letter));
            }
        }
        cout << filtered;
        for (int i = 0; i < filtered.size() / 2; i++) {
            if(filtered[i] != filtered[filtered.size()-i-1]) {
                return false;
            }
        }
        return true;
    }
};
