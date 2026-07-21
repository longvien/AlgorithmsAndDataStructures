#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
typedef long long ll;
vector<bool> SieveOfEratosthenes(ll n) {
    vector<bool> arr(n+1, true);
    arr[0] = false;
    arr[1] = false;
    for(ll i = 2; i<(ll)sqrt(n)+1; i++) {
        if (arr[i]) {
            for (ll k = i*i; k < n+1; k+=i) {
                arr[k] = false; 
            }
        }
    }
    return arr;
}

int main() {
    int x;
    cin >> x;
    if (x==1) {cout << "No Prime number in range 1 -> " << x << "\n";}
    else {
        vector<bool> ans = SieveOfEratosthenes(x); 
        for (ll i = 0; i < ans.size(); i++) {
            if (ans[i]) { cout << i << " ";}
        } 
    }
    cout << "\n";
    return 0;
}


/*To check if n is a prime number, you must only iterate from 2 to √n 
and check during the iteration if it's remainder to any num is 0, if yes => not prime num*/