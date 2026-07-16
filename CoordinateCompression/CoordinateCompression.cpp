#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")

int main() {
    int n;
    cin >> n;
    vector<int> in;
    for (int i=0;i<n;i++) {
        int num;
        cin>>num;
        in.push_back(num);
    }
    vector<int> copy = in;
    sort(copy.begin(), copy.end());
    copy.erase(unique(copy.begin(), copy.end()), copy.end());
    unordered_map<int, int> idx;
    for (int i=0;i<copy.size();i++) {
        idx[copy[i]]=i;
    }
    for (int i=0;i<in.size();i++) {
        in[i] = idx[in[i]];
    }
    for (auto& n:in) {
        cout << n << " ";
    }
    return 0;
}  
/* std::unique is used to remove adjacent duplicate elements. 
To delete every duplicates, sort the arr first! */