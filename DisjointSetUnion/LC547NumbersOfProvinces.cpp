#include<bits/stdc++.h>
using namespace std;
#define f(i,a,n) for(int i = a; i<n; i++)
class Solution {
public:
    int c;
    vector<int> p;
    int find(int x) {
        if (p[x]==x)return x;
        return p[x]=find(p[x]);
    }
    void join(int a, int b) {
        int p1=find(a),p2=find(b);
        if (p1!=p2) {
            p[p1]=p2;
            c--;
        }
    }
    int findCircleNum(vector<vector<int>>& matrix) {
        p = vector<int>(matrix.size()),c = matrix.size();
        f(i,0,matrix.size()) p[i]=i;
        f(i,0,matrix.size()) {
            f(j,i,matrix.size()) {
                if(matrix[i][j]==1) join(i,j);
            }
        }
        return c;
    }
};