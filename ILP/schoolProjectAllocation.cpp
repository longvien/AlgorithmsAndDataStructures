#include <ortools/sat/cp_model.h>
#include <iostream>
#include <vector>

using namespace operations_research;
using namespace std;
using namespace sat;

int main() {
    CpModelBuilder model;
    vector<string> name = {"Anna", "Ben", "Chris", "Dana"};
    vector<vector<int>> projects = {{9, 3, 7, 5}, {2, 8 ,6, 7}, {6, 5, 9, 3}, {7, 6, 4, 8}};
    vector<vector<BoolVar>> x(4, vector<BoolVar>());
    
    // Decision Variables
    for (int m = 0; m < x.size(); m++) {
        for (int i = 0; i < 4; i++) {
            x[m].push_back(model.NewBoolVar());  // x[i][j] ∈ {0,1} | if st[i] do task j => 1, else 0
        }
    } 
    // Constraits
    for (int z = 0; z < x.size(); z++) {
        LinearExpr tPr;
        for (int i = 0; i < 4; i++) {
            tPr += LinearExpr(x[z][i]);
        }
        model.AddEquality(tPr, 1); // j=1∑4 x[i][j] = 1, i ∈ {1, 2, 3, 4} | Each student is assigned exactly 1 task.
    }
    for (int i = 0; i < 4; i++) {
        LinearExpr tS;
        for (int l = 0; l < x.size(); l++){
            tS += LinearExpr(x[l][i]);
        }
        model.AddEquality(tS, 1); // i=1∑4 x[i][j] = 1, j ∈ {1, 2, 3, 4} | Each task is assigend to exactly 1 student
    }
    model.AddEquality(LinearExpr(x[1][2]), 0); // x[1][2] = 0 | Ben can't do the game project.
    
    // Objective
    LinearExpr tSuitability;
    for (int n = 0; n < x.size(); n++) {
        for (int i = 0; i < 4; i++) {
            tSuitability += LinearExpr(x[n][i]) * projects[i][n];
        }
    }
    model.Maximize(tSuitability); // max j=1∑4 x[i][j] * suitability[j][i], i ∈ {1, 2, 3, 4} | max suitability possible

    CpSolverResponse response = Solve(model.Build());
    cout << "Status: ";
    if (response.status() == CpSolverStatus::OPTIMAL) {cout << "Optimal \n";}
    else if (response.status() == CpSolverStatus::FEASIBLE) {cout << "Feasible \n";}
    else {cout << "Infeasible \n";}
    
    for (int i = 0; i < x.size(); i++ ) {
        cout << name[i] << ": ";
        for (const BoolVar& n : x[i]) {
            cout << SolutionBooleanValue(response, n) << " ";
        }
        cout << "\n";
    }
    cout << "Optimal Suitability: " << response.objective_value();
}