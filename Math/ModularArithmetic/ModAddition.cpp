#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll modAddition(ll a, ll b, ll m) {
    return (a%m + b%m)%m;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll a, b, m;
    cin >> a >> b >> m;
    cout << modAddition(a, b, m) << "\n";
    return 0;
}

