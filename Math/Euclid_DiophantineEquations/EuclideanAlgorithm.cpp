#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
typedef long long ll;

ll Euclidean(ll a , ll b) {
    if (b == 0) {return a;}
    return Euclidean(b, a%b);
}
int main() {
    ll a, b;
    cin >> a >> b;
    cout << Euclidean(a, b) << "\n";
}