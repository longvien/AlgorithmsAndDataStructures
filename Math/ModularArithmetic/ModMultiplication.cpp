#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
typedef long long ll;

ll modMultiplication(ll a, ll b, ll m) {
    return (a%m * b%m) %m;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll a, b , m;
    cin >> a >> b >> m;
    cout << modMultiplication(a, b, m) << "\n";
    return 0;
}