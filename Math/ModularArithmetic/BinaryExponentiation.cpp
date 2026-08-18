#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#pragma GCC optimize("O3")

ll fastPow(ll a, ll b, ll m) {
    ll ans = 1;
    a%=m;
    while (b>0) {
        if (b&1) {
            ans = ((__int128)ans*a)%m; 
        }
        a = ((__int128)a*a)%m;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll ans = fastPow(1e18, 1e18, 90);
    cout << ans << "\n";
    return 0;
}