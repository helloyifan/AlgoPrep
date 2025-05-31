#include <vector>
#include <iostream>
using namespace std;

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
struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr) {
            vector<int> emptyVector = {};
            return emptyVector;
        }
        
        vector<int> left = inorderTraversal((*root).left);
        cout << (*root).left->val;
        vector<int> right = inorderTraversal((*root).right);
        
        vector<int> retVal = {};
        if (!left.empty()) {
            retVal.insert(retVal.end(), left.begin(), left.end());
        }

        if (!right.empty()) {
            retVal.insert(retVal.end(), right.begin(), right.end());
        }

        return retVal;
    }   
};


// int main() {
//     Solution sol;
//     vector<string> input = {"flower","flow","flight"};
//     string ret = sol.longestCommonPrefix(input);
//     cout << ret << endl;

// };