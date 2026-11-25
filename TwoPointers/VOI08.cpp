/**
 *    author:  l513n
 *    created: 25.11.2026 15:38:32
**/
#pragma GCC optimize("O3")
#include <bits/stdc++.h>

using namespace std;

#define int long long
#define elif else if
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
    int n;
    cin >> n;
    vector<int> a, b;
    f(i,0,n) {
        int curr;
        cin >> curr;
        a.push_back(curr);
    }
    f(i,0,n) {
        int curr;
        cin >> curr;
        b.push_back(curr);
    }
    sort(all(a));
    sort(all(b));
    int l = 0, r = n-1, ans = numeric_limits<int>::max();
    while (l<n&&r>=0) {
        ans = min(ans, abs(a[l]+b[r]));
        if (b[r] > -a[l]) {
            r--;
        } else {
            l++;
        }
    }
    cout << ans << endl;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    solve();
    return 0;
}
