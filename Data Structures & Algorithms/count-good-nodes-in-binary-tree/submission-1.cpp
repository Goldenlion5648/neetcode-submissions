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
public:
    int goodNodes(TreeNode* root) {
        return helper(root, INT_MIN);
        
    }

    int helper(TreeNode* cur, int prev_hi) {
        if (!cur) {
            return 0;
        }
        int cur_val = cur->val >= prev_hi;
        prev_hi = max(prev_hi, cur->val);
        return cur_val + helper(cur->left, prev_hi) + helper(cur->right, prev_hi);
    }
};








