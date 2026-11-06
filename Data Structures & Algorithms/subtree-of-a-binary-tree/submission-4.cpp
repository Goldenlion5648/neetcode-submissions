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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        return isSame(root, subRoot) || (
            root && (
                isSubtree(root->left, subRoot) || 
                isSubtree(root->right, subRoot)
            )
        );
    }

    bool isSame(TreeNode* first, TreeNode* second) {
        if (bool(first) ^ bool(second)) {
            return false;
        }
        if (!bool(first)) {
            return true;
        }
        if (first->val != second->val) {
            return false;
        }

        return isSame(first->left, second->left) && isSame(first->right, second->right);

    }
};

