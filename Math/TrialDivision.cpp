#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")


bool TrialDivision(int n) {
    for (int i = 2; i < (int)sqrt(n)+1; i++) {
        if (n%i == 0) {
            return false;
        }
    }
    return true;
}
int main() {
    int x;
    cin >> x;
    string ans = (TrialDivision(x) == 1)? "Is Prime!" : "Is not Prime";
    cout << ans;
    return 0;
}

/*To check if n is a prime number, you must only iterate from 2 to √n 
and check during the iteration if it's remainder to any num is 0, if yes => not prime num*/