#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#pragma GCC optimize("O3")

namespace FastIO {
    inline void init() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    }
}
signed main() {
    FastIO::init();
    ll x, mask, i;
    ll popCount;
    cin >> x >> mask >> i;
    cin >> popCount;
    if (x&(mask<<i)) cout << "Bit " << i << " of " << x << " = 1\n"; // if bit i of x is 1
    else cout << "Bit " << i << " of " << x << " is not 1\n"; // if bit i of x = 0
    x|=(mask<<i+1); // set bit i+1 of x to 1
    cout << x << "\n";
    x^=(mask<<i+2); // flip bit i+1 of x
    cout << x << "\n";
    x&=~(mask<<i+3); // clear bit i+3 of x
    cout << x << "\n";
    cout << "The number of bit 1 in " << popCount << " is " << __builtin_popcount(popCount) << "\n";
    return 0;
}








