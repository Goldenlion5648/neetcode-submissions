struct Node {
    int key;
    int value;
};

class LRUCache {
    int cap;
    list<Node> nodes;
    unordered_map<int, list<Node>::iterator> num_to_node_pos;
public:
    LRUCache(int capacity): cap(capacity) {
        
    }
    
    int get(int key) {
        if (!num_to_node_pos.contains(key)) {
            return -1;
        }
        auto old_node_pos = num_to_node_pos[key];
        nodes.splice(nodes.end(), nodes, num_to_node_pos[key]);
        return num_to_node_pos[key]->value;
    }
    
    void put(int key, int value) {
        if (num_to_node_pos.contains(key)) {
            nodes.erase(num_to_node_pos[key]);
        }
        Node new_node{key, value};
        nodes.push_back(new_node);
        num_to_node_pos[key] = prev(nodes.end());
        if (num_to_node_pos.size() > this->cap) {
            int old_key = num_to_node_pos[nodes.begin()->key]->key;
            nodes.erase(nodes.begin());
            num_to_node_pos.erase(old_key);
        }
    }
};
