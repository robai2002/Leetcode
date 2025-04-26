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
    void solve(TreeNode* root, int len,int &maxlen){
        if(root==NULL){
            return;
        }else if(root->left==NULL && root->right==NULL){
            if(len>maxlen){
                maxlen=len;
            }
        }
        solve(root->left,len+1,maxlen);
        solve(root->right,len+1,maxlen);
    }
    int maxDepth(TreeNode* root) {
        /*For Root Node declare len as 1*/
        int len=1;
        int maxlen=0;
        solve(root,len,maxlen);
        return maxlen;
    }
};