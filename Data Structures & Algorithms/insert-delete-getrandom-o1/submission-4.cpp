class RandomizedSet {
    unordered_map<int, int> val_to_index;
    vector<int> values;
public:
    RandomizedSet() {
    }
    
    bool insert(int val) {
        bool was_new = val_to_index.count(val) == 0;
        if (was_new) {
            val_to_index[val] = (int)values.size();
            values.push_back(val);
        }
        return was_new;
    }
    
    bool remove(int val) {
        bool was_present = val_to_index.count(val) > 0;
        if (was_present) {
            int old_pos = val_to_index[val];
            val_to_index.erase(val);
            int last_value = values.back();
            if (last_value == val) {
                values.pop_back();
                return was_present;
            }
            values[old_pos] = values.back();
            val_to_index[last_value] = old_pos;
            values.pop_back();
        }
        return was_present;
    }
    
    int getRandom() {
        return values[rand() % values.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */