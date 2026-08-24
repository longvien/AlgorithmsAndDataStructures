#include <bits/stdc++.h>
using namespace std;
//#pragma GCC optimize("O3")
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

int solve (unordered_map<char, vector<pair<char, int>>> graph, char start, vector<char> cities, int indexStartCity) {
    int numOCities = cities.size();
    int p = fastpow(2,numOCities);
    matrix<int> dp(p, vector<int>(numOCities, numeric_limits<int>::max()));
    dp[(1<<indexStartCity)][indexStartCity] = 0;
    for (int mask=(1<<indexStartCity); mask<(1<<numOCities); mask++) {
        for (int curr=0; curr<numOCities; curr++) {
            if (mask&(1<<curr) && (dp[mask][curr] != numeric_limits<int>::max())) {
                for (int next=0; next<numOCities; next++) {
                    if (!(mask&(1<<next))) {
                        int newMask = mask|(1<<next);
                        int cost = 0;
                        char nextS = cities[next];
                        for (int i = 0; i < graph[cities[curr]].size(); i++) {
                            if (graph[cities[curr]][i].fi==cities[next]) {
                                cost = graph[cities[curr]][i].se; 
                                break;
                            }
                        }
                        dp[newMask][next] = min(dp[newMask][next], dp[mask][curr]+cost);
                    }
                }
            }   
        }
    }
    int ans = numeric_limits<int>::max();
    for (int i = 0; i<numOCities; i++) {
        if (cities[i]==start) continue;
        for (int j = 0; j<graph[cities[i]].size(); j++) {
            if (graph[cities[i]][j].fi == start) ans = min(ans, dp[p-1][i]+graph[cities[i]][j].se);
        }      
    }
    return ans;
}

signed main() {
    FastIO::init();
    int numCities = 4;
    // cin >> numCities;
    char startPoint = 'A';
    // cin >> startPoint;
   unordered_map<char, vector<pair<char, int>>> graph = {
    {'A', {{'B', 10}, {'C', 15}, {'D', 20}}},
    {'B', {{'A', 10}, {'C', 35}, {'D', 25}}},
    {'C', {{'A', 15}, {'B', 35}, {'D', 30}}},
    {'D', {{'A', 20}, {'B', 25}, {'C', 30}}}
    };
    vector<char> cities = {'A', 'B', 'C', 'D'};
    int indexStartCity = 0;
    // for (int i = 0; i < numCities; i++) {
    //     char root;
    //     cin >> root;
    //     cities.push_back(root);
    //     if (root==startPoint) indexStartCity = i;
    //     graph[root] = vector<pair<char, int>>();
    //     for (int j = 0; j<numCities-1; j++) {
    //         char c;
    //         int co;
    //         cin >> c >> co;
    //         graph[root].push_back({c, co});
    //     }
    //     cout << root << "\n";
    // }
    cout << solve(graph, startPoint, cities, indexStartCity) << "\n";
    return 0;
}