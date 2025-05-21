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
    bool solve(TreeNode* r1, TreeNode* r2)   {
        if(!r1 && !r2)    return true;
        if(r1 && !r2)   return false;
        if(!r1 && r2)   return false;
        
        return (r1->val == r2->val) && solve(r1->left, r2->right) && solve(r1->right, r2->left);
    }

    bool isSymmetric(TreeNode* root) {
        if(!root || (!root->left && !root->right))  return true;
        return solve(root->left, root->right);
    }
};