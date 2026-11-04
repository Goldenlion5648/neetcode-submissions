class Node {
public:
    unordered_map<char, Node*> keys;
    Node() {
    }
    
    ~Node() {
        for (auto& [key, value] : keys) {
            delete value;
        }
    }

    Node* add_new(char letter) {
        if(keys.count(letter) == 0) {
            keys[letter] = new Node();
        }
        return keys[letter];
    }
};

class PrefixTree {
public:
    Node* start;
    static constexpr char END = '#';
    PrefixTree() {
        start = new Node();
    }
    
    void insert(string word) {
        Node* cur = start;
        for(const auto& letter : word) {
            cur = cur->add_new(letter);
        }
        cur->keys[END] = nullptr;
    }
    
    bool search(string word) {
        Node* cur = start;
        for(const auto& letter : word) {
            if (cur->keys.count(letter) == 0) {
                return false;
            } 
            cur = cur->add_new(letter);
        }
        return cur->keys.count(END) == 1;
    }
    
    bool startsWith(string prefix) {
        Node* cur = start;
        for(const auto& letter : prefix) {
            if (cur->keys.count(letter) == 0) {
                return false;
            } 
            cur = cur->add_new(letter);
        }
        return true;
    }
};
