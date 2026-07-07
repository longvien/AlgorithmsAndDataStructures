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
#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        deque<vector<int>> queue;
        deque<vector<TreeNode*>> queue2;
        if (root) {
            queue.push_back({root->val});
            queue2.push_back({root});
            while (!queue.empty()) {
                vector<int> curr = queue.front();
                queue.pop_front();
                vector<TreeNode*> curr2 = queue2.front();
                queue2.pop_front();
                ans.push_back(curr);
                for (const auto& i : curr2) {
                    if (i->left != nullptr) {
                        if (queue.empty()) {
                            queue.push_back({});
                            queue2.push_back({});
                        }
                        queue[0].push_back(i->left->val);
                        queue2[0].push_back(i->left);
                    }
                    if (i->right != nullptr) {
                        if (queue.empty()) {
                            queue.push_back({});
                            queue2.push_back({});
                        }
                        queue[0].push_back(i->right->val);
                        queue2[0].push_back(i->right);
                    }

                }
            }

        }
        return ans;
    }
};