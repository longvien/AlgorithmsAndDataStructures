#include <bits/stdc++.h>
using namespace std;
#pragma GCC optimize("O3")
#define fi first
#define se second
template <typename T>
using matrix = vector<vector<T>>;
template <typename T>
T fastpow(T a, T b) {
    T ans=1;
    while(b>0) {
        if (b&1) ans*=a;
        a*=a;
        b>>=1;
    }
    return ans;
}
namespace FastIO {
    inline void init() {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);
    }
}

int solve (const vector<vector<int>>& cost, vector<char>& cities, int& indexStartCity) {
    int numOCities = cities.size();
    int p = fastpow(2,numOCities);
    matrix<int> dp(p, vector<int>(numOCities, numeric_limits<int>::max()));
    dp[(1<<indexStartCity)][indexStartCity] = 0;
    for (int mask=(1<<indexStartCity); mask<(1<<numOCities); mask++) {
        if (!(mask&(1<<indexStartCity))) continue; // Reachability
        for (int curr=0; curr<numOCities; curr++) {
            if (mask&(1<<curr) && (dp[mask][curr] != numeric_limits<int>::max())) {
                for (int next=0; next<numOCities; next++) {
                    if (!(mask&(1<<next))) {
                        int newMask = mask|(1<<next);
                        dp[newMask][next] = min(dp[newMask][next], dp[mask][curr]+cost[curr][next]);
                    }
                }
            }   
        }
    }
    int ans = numeric_limits<int>::max();
    for (int i = 0; i<numOCities; i++) {
        if (cities[i]==cities[indexStartCity]) continue;
        ans = min(ans, dp[p-1][i]+cost[i][indexStartCity]);
    }
    return ans;
}

signed main() {
    FastIO::init();
    int numCities;
    cin >> numCities;
    char startPoint;
    cin >> startPoint;
    vector<vector<int>> graph(numCities, vector<int>());
    vector<char> cities;
    int indexStartCity = 0;
    for (int i = 0; i < numCities; i++) {
        char root;
        cin >> root;
        cities.push_back(root);
        if (root==startPoint) indexStartCity = i;
        for (int j = 0; j<numCities; j++) {
            int cost;
            cin >> cost;
            graph[i].push_back(cost);
        }
    }
    cout << solve(graph, cities, indexStartCity) << "\n";
    return 0;
}


