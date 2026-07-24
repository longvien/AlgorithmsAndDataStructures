#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
#define PB push_back
typedef long long ll;

vector<ll> LinearSieve(ll n) /*Euler's Sieve */ { 
    vector<ll> primes;
    vector<ll> spf(n+1, 0); // use int instead of ll inccase n < 1e7 for efficientcy (4 instead of 8 bytes / ele.).
    for (ll i = 2; i < n+1; i++) {
        if (spf[i]==0) {
            primes.PB(i);
            spf[i] = i;
        }
        for (ll& p:primes) {
            if (i*p > n) {break;}
            spf[i*p] = p;
            if (spf[i] == p) {
                break;
            }
        }
    }
    return spf;
}

int main() {
    ll n;
    cin >> n;
    vector<ll> ans = LinearSieve(n);
    for (ll i = 1; i < ans.size(); i++) {
        if (ans[i] == i) { cout << i << " ";}
    }
    cout << "\n";
    return 0;
}

// O(n)