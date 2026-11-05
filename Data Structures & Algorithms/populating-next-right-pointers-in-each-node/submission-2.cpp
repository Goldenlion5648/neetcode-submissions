/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if (!root) {
            return nullptr;
        }
        bfs(root);
        return root;
    }

    void bfs(Node* start) {
        deque<Node*> fringe({start});
        deque<Node*> next_row;
        int goal_size = 1;
        while (fringe.size() > 0) {
            while (fringe.size() > 0) {
                auto cur = fringe.front();
                fringe.pop_front();
                if (fringe.size() > 0) {
                    cur->next = fringe.front();
                } 
                else {
                    cur->next = nullptr;
                }
                if (cur->left) {
                    next_row.push_back(cur->left);
                    next_row.push_back(cur->right);
                }

            }
            swap(fringe, next_row);
        }
    }
};








