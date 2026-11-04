class Node {
public:
    unordered_map<char, std::unique_ptr<Node>> keys;
    Node() {
    }
    

    Node* add_new(char letter) {
        if(keys.count(letter) == 0) {
            keys[letter] = std::make_unique<Node>();
        }
        return keys[letter].get();
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
