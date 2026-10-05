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
      TreeNode* invertTree(TreeNode* root) {
         auto invert = [](TreeNode *curr, auto &invert){
            if(curr == nullptr) return;
            auto L = curr->left;
            auto R = curr->right;
            curr->left = R;
            curr->right = L;
            invert(L, invert);
            invert(R, invert);
         };
         auto curr = root;
         invert(root, invert);
         return root;
      }
};
