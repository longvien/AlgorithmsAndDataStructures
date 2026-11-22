#include <bits/stdc++.h>
using namespace std;

#define ll long long
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

using i128 = __int128_t;
void solve(vector<int> v1, vector<int> v2, int n, int m) {
    int l = 0, r = 0;
    vector<int> ans(n+m);
    ans[0] = min(v1[0], v2[0]);
    
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    return 0;
}
// #end my Template
