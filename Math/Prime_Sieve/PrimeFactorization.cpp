#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#pragma GCC optimize("O3")
#define pb push_back
#define fi first
#define se second
vector<pair<ll, ll>> PrimeFactor(ll n) {
    vector<pair<ll, ll>> ans;
    for (ll i = 2; i <= n/i; i++) {
        if (n%i == 0) {
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;
    cin >> n;
    if (n==1) {cout << "1 can't be factorize in primes. \n";}
    else {
        vector<pair<ll, ll>> out = PrimeFactor(n);
        cout << n << " = ";
        for (ll i = 0; i < out.size(); i++) {
            cout << out[i].fi << "^" << out[i].se;
            if (i+1 < out.size()) {cout << " * ";}
        }
        cout << "\n";
    }
    return 0;
}