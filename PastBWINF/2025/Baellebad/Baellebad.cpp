#include <bits/stdc++.h>
using namespace std;
//#pragma GCC optimize("O3")
#define f(i,a,n) for (int i = a; i<n; i++)


struct BallData {
    string date;
    unordered_set<int> time;
    int ball;

};

BallData solve() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t;
    cin >> t;
    
    string date;
    unordered_set<int> time;
    int maxBall = 0;

    unordered_map<string, unordered_map<int, int>> m;
    vector<string> daysIW = {"Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"};
    
    f(i,0,daysIW.size()) {
        m[daysIW[i]] = unordered_map<int, int>();
    }

    f(i,0,t) {
        
        string classN, currD;
        int start, end, need;
        
        cin >> classN >> currD >> start >> end >> need;
        
        f(j,start,end+1) {
            m[currD][j] = (m[currD].count(j) == 0)? need : m[currD][j] + need;
            if (m[currD][j] > maxBall) {
                if (currD == date) {
                    if (time.count(j) == 0) {
                        time.insert(j);
                    }
                }
                if (currD != date) {
                    date = currD;
                    time = {j};
                }
                maxBall = m[currD][j];
            }
        }

    }
    
    return {date, time, maxBall};
}

int main() {
    BallData ans = solve();
    cout << "Man braucht am " << ans[0] << " um"
    for (i,0,ans[1].size()) {
        cout << ans[1][i];
        if (i < ans[1].size()-1) { cout << ", ";}
    }

    cout << " mit eine Anzahl von Bällen: " << ans[3] << "\n";
    return 0;
}