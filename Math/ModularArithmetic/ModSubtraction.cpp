#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#pragma GCC optimize("O3")

ll modSubtraction(ll a, ll b, ll m) {
    return (a%m - b%m+m)%m;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll a, b, m;
    cin >> a >> b >> m;
    cout << modSubtraction(a,b,m) << "\n";
    return 0;
}