#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
typedef long long ll;
#define PB push_back
vector<bool> SegmentedSieve(ll l , ll r) {
    ll limit = (ll)sqrt(r);
    vector<bool> arr(limit+1, true);
    arr[0] = false;
    arr[1] = false;
    for (ll i = 2; i < (ll)sqrt(limit)+1; i++) {
        if (arr[i]) {
            for (ll k = i*i; k < limit+1; k+=i) {
                arr[k] = false;
            }
        }
    }
    vector<ll> prime;
    for (ll i = 2; i < limit+1; i++) {
        if (arr[i]) {prime.PB(i);}
    }
    vector<bool> ans(r-l+1, true);
    if (l == 1) {ans[0] = false;}
    for (ll i = 0; i < prime.size(); i++) {
        ll first_multiple = max(prime[i]*prime[i], ((l+prime[i]-1)/prime[i])*prime[i]);
        for (ll j = first_multiple; j<r+1; j+=prime[i]) {
            ans[j-l] = false;
        }
    }
    return ans;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll l, r;
    cin >> l >> r;
    vector<bool> k = SegmentedSieve(l, r);
    for (ll i = 0; i < k.size(); i++) {
        if (k[i]) {cout << l+i << " ";}
    }
    cout << "\n";
    return 0;
}