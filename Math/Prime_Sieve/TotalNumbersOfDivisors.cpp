#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define se second
vector<pair<ll, ll>> PrimeFactor(ll n) {
    vector<pair<ll, ll>> ans;
    for (ll i = 2; i <= n/i; i++) {
        if (n%i==0) {
            ll count = 0;
            while (n%i==0) {
                count++;
                n/=i;
            }
            ans.pb({i, count});
        }
    }
    if (n>1) {ans.pb({n, 1});}
    return ans;
}

ll numOfDivisors(ll n) {
    ll totalDiv = 1;
    vector<pair<ll, ll>> res = PrimeFactor(n);
    for (int i = 0; i < res.size(); i++) {
        totalDiv *= res[i].se+1;
    }
    return totalDiv;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;
    cin >> n;
    cout << n << " has total of " << numOfDivisors(n) << " divisors.\n";
}
/*calc d(N) using prime factorization and combinatorics.*/