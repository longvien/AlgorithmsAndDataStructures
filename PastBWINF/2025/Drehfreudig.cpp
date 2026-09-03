#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")

namespace FastIO {
    inline void init() {
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);
    }
}

struct AdjRoot {
    unordered_map<int, vector<int>> AdjList;
    int RootNode;
};

AdjRoot AdjacencyListSplitter(string& in) {
    unordered_map<int, vector<int>> adj;
    int root = 1;
    deque<int> CurrPastParent;
    int parent = 0, curr = 1;
    int latest = curr;
    adj[1] = vector<int>();
    for (int i = 1; i < in.size(); i++) {
        if (in[i] == '(') {
            CurrPastParent.push_back(parent);
            parent = curr;
            curr = latest+1;
            latest = curr;
            if (adj.count(curr)==0) adj[curr] = vector<int>();
        }
        else if (in[i] == ')' && curr != 1) {
            adj[parent].push_back(curr);
            curr = parent;
            parent = CurrPastParent.back();
            CurrPastParent.pop_back();
        }
    }
    AdjRoot ans;
    ans.AdjList = adj;
    ans.RootNode = root;
    return ans;
}

vector<pair<int ,int>> CountDivFactorOfLeafNodes(unordered_map<int, vector<int>>& tree, int& root) {
    vector<pair<int, int>> DivFactorOfLeaf;
    unordered_map<int, int> DivFact;
    queue<int> q;
    unordered_set<int> visited = {root};
    q.push(root);
    DivFact[root] = 1;

    while (!q.empty()) {
        int curr = q.front();
        q.pop();
        if (tree[curr].size() == 0)  {
            DivFactorOfLeaf.push_back({curr, DivFact[curr]});
            continue;
        }
        for (int i = 0; i < tree[curr].size(); i++) {
            if (visited.count(tree[curr][i])==0) {
                q.push(tree[curr][i]);
                visited.insert(tree[curr][i]);
                DivFact[tree[curr][i]] = DivFact[curr] * tree[curr].size();
            }
        }
    }
    return DivFactorOfLeaf;
}


bool CheckIfDrehfreudig(vector<pair<int, int>>& DivFactor) {
    for (int i = 0; i <= DivFactor.size()/2; i++) {
        if (DivFactor[i].second != DivFactor[DivFactor.size()-i-1].second) {
            return false;
        }
    }
    return true;
}

signed main() {
    FastIO::init();
    string input;
    cin >> input;
    AdjRoot AdjListAndRoot = AdjacencyListSplitter(input);
    unordered_map<int, vector<int>> adj = AdjListAndRoot.AdjList;
    int root = AdjListAndRoot.RootNode;
    if (adj[root].size() == 0) {
        cout << "Drehfreudig \n";
        return 0;
    }
    else if (adj[root].size() < 2) {
        cout << "Nicht Drehfreudig \n";
        return 0;
    }
    vector<pair<int, int>> LeafNodesDivFactor = CountDivFactorOfLeafNodes(adj, root);
    bool drehfreudig = CheckIfDrehfreudig(LeafNodesDivFactor);
    cout << ((drehfreudig)? "Drehfreudig" : "Nicht Drehfreudig") << "\n";
    return 0;
}


