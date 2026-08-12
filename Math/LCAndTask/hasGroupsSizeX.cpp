#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        sort(deck.begin(), deck.end());
        bool ans = true;
        int countCurr = 0, first = 0, gcdPrev = 0;
        for (int i = 0; i < deck.size(); i++) {
            if (i>=1 && deck[i]!=deck[i-1]) {
                if (first>=1) {
                    gcdPrev = gcd(countCurr, gcdPrev);
                    if (gcdPrev == 1) {
                        ans = false;
                        break;
                    }
                    countCurr = 1;
                    continue;
                }
                else {
                    gcdPrev = countCurr;
                    countCurr = 1;
                    first++;
                    continue;
                }
            }
            countCurr++;
        }
        return (gcd(countCurr, gcdPrev) == 1)? false : ans;
    }
};