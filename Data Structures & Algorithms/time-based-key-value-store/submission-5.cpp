struct TimeAndValue {
    int time;
    string value;
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
            [](int time, TimeAndValue cur) {
                return time < cur.time;
            }
        );
        if (found == seen[key].begin()) {
            return "";
        } 
        return prev(found)->value;
    }
};
