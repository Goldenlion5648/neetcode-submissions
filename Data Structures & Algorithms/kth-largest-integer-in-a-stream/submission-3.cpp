class KthLargest {
    priority_queue<int, vector<int>, greater<int>> values;
    int cap;
public:
    KthLargest(int k, vector<int>& nums) {
        cap = k;
        for (const auto& num : nums) {
            add(num);
        }

    }
    
    int add(int val) {
        values.push(val);
        if (values.size() > cap) {
            values.pop();
        }
        return values.top();
    }
};
