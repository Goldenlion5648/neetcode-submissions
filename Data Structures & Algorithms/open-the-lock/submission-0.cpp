using Digits = array<int, 4>;

struct Combo {
    Digits combo;
    int steps;
};
class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        set<Digits> bad_spots;
        for (const auto& dead_spot : deadends) {
            bad_spots.insert(Digits{
                dead_spot[0]-'0', 
                dead_spot[1]-'0', 
                dead_spot[2]-'0', 
                dead_spot[3]-'0', 
            });
        }
        set<Digits> seen;
        deque<Combo> fringe;
        fringe.push_back(Combo{{0,0,0,0}, 0});
        Digits goal{
            target[0]-'0', 
            target[1]-'0', 
            target[2]-'0', 
            target[3]-'0', 
        };
        while (!fringe.empty()) {
            auto cur = fringe.front();
            fringe.pop_front();
            if (bad_spots.contains(cur.combo)) {
                continue;
            }
            if (cur.combo == goal) {
                return cur.steps;
            }
            if (seen.count(cur.combo) > 0) {
                continue;
            }
            seen.insert(cur.combo);
            for (int i = 0; i < 4; i++) {
                for (auto diff : {-1, 1}) {
                    Digits temp = cur.combo;
                    temp[i] = (temp[i] + diff) % 10;
                    if (temp[i] < 0) {
                        temp[i] = 9;
                    }
                    fringe.push_back(Combo{temp, cur.steps + 1});
                }
            }
        }
        return -1;
    }
};