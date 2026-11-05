/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    unordered_map<TreeNode*, int> cache;
public:
    bool isBalanced(TreeNode* root) {
        if (!root) {
            return true;
        }
        int left = getDepth(root->left);
        int right = getDepth(root->right);
        return abs(left - right) <= 1 && isBalanced(root->left) && isBalanced(root->right);

    }

    int getDepth(TreeNode* cur) {
        if (!cur) {
            return 0;
        }
        if (cache.contains(cur)) {
            return cache[cur];
        }
        cache[cur] = 1 + max(getDepth(cur->left), getDepth(cur->right));
        return cache[cur];
    }
};






