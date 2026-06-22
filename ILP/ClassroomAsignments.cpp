#include <ortools/sat/cp_model.h>
#include <vector>
#include <iostream>

using namespace operations_research;
using namespace sat;
using namespace std;

int main() {
    CpModelBuilder model;
    vector<string> name = {"Anna", "Ben", "Chris", "Dana", "Emma", "Felix"};
    vector<string> classN = {"Room A", "Room B", "Room C"};
    vector<int> limit = {2, 3, 2};
    vector<vector<int>> pfrScores = {{9, 3, 6}, {4, 8, 5}, {7, 5, 9}, {6, 7, 4}, {8, 6, 5}, {3, 9, 7}};
    vector<vector<BoolVar>> x(name.size(), vector<BoolVar>());
    
    for (int i = 0; i < name.size(); i++) {
        for (int n = 0; n < classN.size(); n++) {
            x[i].push_back(model.NewBoolVar()); // x[i][j] ∈ {0,1}
        }
    }

    for (int i = 0; i < name.size(); i++) {
        LinearExpr tClass;
        for (int j = 0; j < classN.size(); j++) {
            tClass += LinearExpr(x[i][j]); 
        }
        model.AddEquality(tClass, 1); // j=0∑2 x[i][j] = 1, i ∈ {0, 1, 2, ... 5}
    }

    for (int j = 0; j < classN.size(); j++) {
        LinearExpr tSt;
        for (int i = 0; i < name.size(); i++) {
            tSt += LinearExpr(x[i][j]);
        }
        model.AddLessOrEqual(tSt, limit[j]); // i=0∑5 x[i][j] <= limit[j], j ∈ {0, 1, 2}
    }

    model.AddEquality(LinearExpr(x[1][2]), 0);

    LinearExpr tPfrScore;
    for (int i = 0; i < name.size(); i++) {
        for (int j = 0; j < classN.size(); j++) {
            tPfrScore += LinearExpr(x[i][j]) * pfrScores[i][j];
        }
    }

    model.Maximize(tPfrScore);

    CpSolverResponse response = Solve(model.Build());
    cout << "Status: ";
    if (response.status() == CpSolverStatus::OPTIMAL) {cout << "Optimal\n";}
    else if (response.status() == CpSolverStatus::FEASIBLE) {cout << "Feasible\n";}
    else {cout << "Infeasible\n";}

    for (int j = 0; j < classN.size(); j++) {
        cout << classN[j] << ": ";
        for (int i = 0 ; i < name.size(); i++) {
            if (SolutionBooleanValue(response, x[i][j]) == 1) {
                cout << name[i] << " ";
            }
        }
        cout << "\n";
    }

    cout << "Maximum Satisfaction Score: " << response.objective_value();
    return 0;
}