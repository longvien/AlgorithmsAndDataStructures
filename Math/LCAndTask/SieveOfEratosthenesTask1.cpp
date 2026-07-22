#include <bits/stdc++.h>
using namespace std;
using namespace std::chrono;
#pragma GCC optimize("O3")
typedef long long ll;

vector<bool> solve(ll n) {
    vector<bool> ans(n+1, true);
    ans[0] = false;
    ans[1] = false;
    for (ll i = 2; i < (ll)sqrt(n)+1; i++) {
        if (ans[i]) {
            for (ll k = i*i; k<n+1; k+=i) {
                ans[k] = false;
            } 
        }
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;
    cin >> n;
    auto start = high_resolution_clock::now();
    if (n==1) {
        cout << "No Prime Number in range 1->1, Max diff: 0 \n";
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(stop - start);
        cout << "\nExecution Time: " << duration.count() << " ms\n";
    }
    else {
        vector<bool> res = solve(n);
        int diff = 0;
        int curr = 2;
        int prev = 2;
        for (int i = 0; i < res.size(); i++) {
            if (res[i]) {
                prev = curr;
                curr = i;
                diff = max({diff, curr-prev});
            }
        } 
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(stop - start);
        cout << "Prime numbers in range from 1 -> " << n << ": \n";
        for (int i = 0; i < res.size(); i++) {
            if (res[i]) {cout << i << " ";}
        }
        cout << "\n";
        cout << "Max Difference: " << diff << "\n";
        cout << "\nExecution Time: " << duration.count() << " ms\n";
    }
    return 0;
}