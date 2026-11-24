/**
 *    author:  l513n
 *    created: 24.11.2026 22:29:50
**/
#pragma GCC optimize("O3")
#include <bits/stdc++.h>

using namespace std;

#define int long long
#define elif else if
#define str string
#define endl "\n"
#define MOD 1000000007
#define EPS 0.000000001
#define all(x) x.begin(), x.end()
#define len(x) (int)x.size()
#define sqr(x) ((x) * (x))
#define cube(x) ((x) * (x) * (x))
#define low_bit(x) ((x) & (-(x)))
#define srt(x) sort(all(x))
#define maxel(x) *max_element(all(x))
#define minel(x) *min_element(all(x))
#define sum(x) accumulate(all(x), 0LL)
#define pb push_back
#define mp make_pair
#define is_even(x) ((x & 1) == 0)
#define is_odd(x)  ((x & 1) == 1)
#define f(i, a, n) for (int i = a; i < n; i++)

template <typename T>
using matrix = vector<vector<T>>;
template <typename T>
using max_heap = priority_queue<T, vector<T>, less<T>>;
template <typename T>
using min_heap = priority_queue<T, vector<T>, greater<T>>;
void solve() {
    str n;
    cin >> n;
    vector<char> o, e;
    for (int i = 0; i < len(n); i++) {
        int nN = static_cast<int>(n[i]) - 48;
        if (nN%2==0) {
            e.push_back(n[i]);
        } else {
            o.push_back(n[i]);
        }
    }
    str ans = "";
    int l = 0, r = 0;
    while (l!=len(o) && r!=len(e)) {
        int nL = static_cast<int>(o[l]) - 48, nR = static_cast<int>(e[r]) - 48;
        if (nL < nR) {
            ans += o[l];
            l++;
        } else {
            ans += e[r];
            r++;
        }
    }
    if (l==len(o)&&r!=len(e)) {
        for (; r < len(e); r++) {
            ans += e[r];
        }
    } else if (l!=len(o)&&r==len(e)) {
        for (; l < len(o); l++) {
            ans += o[l];
        }
    }
    cout << ans << endl;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int m;
    cin >> m;
    while (m--) {
        solve();
    }
    return 0;
}