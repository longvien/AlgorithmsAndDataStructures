#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
typedef long long ll;

ll fastPow(ll a, ll b) {
    ll MOD = 10;
    ll ans = 1;
    a%=MOD;
    while(b>0) {
        if (b&1) {
            ans = ((__int128)a*ans)%MOD;
        }
        a = ((__int128)a*a)%MOD;
        b >>= 1;
    }
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;
    cin >> n;
    cout << fastPow(1378, n)%10 << "\n";
    return 0;
}