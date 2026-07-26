#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
#define pb push_back
ll powInt(ll a, ll b) {
    ll ans = 1;
    for (ll i = 0; i<b; i++) { ans*=a;}
    return ans;
}
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

ll SumOfDiv(ll n) {
    ll sum = 1;
    vector<pair<ll, ll>> res = PrimeFactor(n);
    for (ll i = 0; i < res.size(); i++) {
        sum *= (powInt(res[i].fi, res[i].se+1)-1)/(res[i].fi-1);
    }
    return sum;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n;
    cin >> n;
    ll ans = SumOfDiv(n);
    cout << "Sum Of Divisors: "<< ans << "\n";
    return 0;
}


