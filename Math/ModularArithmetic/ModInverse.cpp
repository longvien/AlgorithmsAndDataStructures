#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

bool isPrime(ll n) {
    for (int i = 2; i < (ll)sqrt(n)+1; i++) {
        if (n%i == 0) {
            return false;
        }
    }
    return true;
}

ll gcd(ll a, ll b) {
    return (b==0)? a: gcd(b, a%b);
}

ll fastPow(ll a, ll p, ll m) {
    ll ans = 1;
    a%=m;
    while (p>0) {
        if (p&1) {
            ans = ((__int128)ans*a)%m;
        }
        a = ((__int128)a*a)%m;
        p>>=1;
    }
    return ans;
}

// find x which (ax) mod m = 1 ; ax = mq + 1; ax - mq = 1; ax + my(-q) = 1 (gcd(a,m))
ll ExtEuclid(ll a, ll b) {
    ll x1 = 1, x2 = 0, x3 = 0;
    ll y1 = 0, y2 = 1, y3 = 0;
    ll q = a/b;
    ll r = a - q*b;
    while (r != 0) {
        a = b;
        b = r;
        x3 = x1 - q*x2;
        y3 = y1 - q*y2;
        x1 = x2;
        y1 = y2;
        x2 = x3;
        y2 = y3;
        q = a/b;
        r = a-q*b;
    }
    return (x2 > -1)? x2: x2+;
}

ll ModDiv(ll a, ll b, ll m) {
    if (gcd(b, m) != 1) {
        if (a%b != 0) { return -1; }
        return (a/b)%m;
    }

    if (isPrime(m)) {
        return ((a%m) * (fastPow(b, m-2, m)))%m;
    }
    return ((a%m) * ExtEuclid(b, m))%m; 
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll a, b, m;
    cin >> a >> b >> m;
    cout << ModDiv(a, b, m) << "\n";
    return 0;
}