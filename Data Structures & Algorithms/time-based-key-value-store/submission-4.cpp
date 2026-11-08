struct TimeAndValue {
    int time;
    string value;
    auto operator<=>(const TimeAndValue& other) const = default;
};
class TimeMap {
public:
    unordered_map<string, vector<TimeAndValue>> seen;
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        seen[key].push_back({
            .time = timestamp,
            .value = value
        });
    }
    
    string get(string key, int timestamp) {
        if (seen[key].size() == 0) {
            return "";
        }

        auto found = upper_bound(
            seen[key].begin(), seen[key].end(), 
            timestamp,
            [](int target, const TimeAndValue& entry) {
                return target < entry.time;
            }
        );
        if (found == seen[key].begin()) {
            return "";
        } 
        return prev(found)->value;
    }
};
