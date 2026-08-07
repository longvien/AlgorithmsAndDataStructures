#include <bits/stdc++.h>
using namespace std;
using ll = signed long long;
#define pb push_back
#pragma GCC optimize("O3")
namespace FastIO {
	inline void init() {
		ios_base::sync_with_stdio(false);
		cin.tie(nullptr);
	}
}

// i =1 ∏ k pi^(ei-1) * (pi-1)
ll phi(ll n) {
    if (n==1) {return 1;}
    ll ans = 1;
    for (ll i=2; i<=n/i; i++) {
        if (n%i==0) {
            while(n%i==0) {
                n/=i;
                ans*=i;
            }
            ans/=i;
            ans*=(i-1);
        }
    }
    if (n>1) { ans *= (n-1); }
    return ans; 
} // Time Complexity: O(√n)

signed main() {
    FastIO::init();
    ll n;
    cin >> n;
    cout << phi(n) << "\n";
    return 0;
}



// 1st Version

// ll fastPow(ll base, ll exponent) {
//     ll ans = 1;
//     while (exponent>0) {
//         if (exponent&1) {
//             ans*=base;
//         }
//         base*=base;
//         exponent>>=1;
//     }
//     return ans;
// }
// vector<pair<ll, ll>> primeFactorization(ll n) {
//     vector<pair<ll, ll>> ans;
//     for (ll i=2; i<=n/i; i++) {
//         if (n%i==0) {
//             ll count = 0;
//             while(n%i==0) {
//                 n/=i;
//                 count++;
//             }
//             ans.pb({i, count});
//         }
//     }
//     if (n>1) { ans.pb({n,1}); }
//     return ans;
// }

// bool isPrime(ll n) {
//     for (ll i = 2; i<=n/i; i++) {
//         if (n%i==0) {return false;}
//     }    
//     return true;
// }

// ll phi(ll n) {
//     if (n==1) {return 1;}
//     if (isPrime(n)) { return n-1; }
//     vector<pair<ll, ll>> rep = primeFactorization(n);
//     ll ans = 1;
//     for (auto& [ba, ex] : rep) {
//         ans = ans*fastPow(ba, ex-1)*(ba-1);
//     }
//     return ans;  
    
// }

// signed main() {
//     FastIO::init();
//     ll n;
//     cin >> n;
//     cout << phi(n) << "\n";
//     return 0;
// }