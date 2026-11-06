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
    bool isSametree(TreeNode* p, TreeNode*q) {
        if (p == nullptr and q == nullptr){
            return true;
        }
        else if (p == nullptr or q == nullptr) {
            return false;
        }

        if (p->val != q->val) {
            return false;
        }
        bool left = isSametree(p->left, q->left);
        bool right = isSametree(p->right, q->right);

        return left and right;
    }

    bool isSubtree(TreeNode* root, TreeNode* subroot) {
        if (subroot == nullptr) {
            return true;
        }
        if (root == nullptr) {
            return false;
        }
        
        if(isSametree(root, subroot)) {
            return true;
        }

        bool left = isSubtree(root->left, subroot);
        bool right = isSubtree(root->right, subroot);
        

        return left or right;
    }
};
