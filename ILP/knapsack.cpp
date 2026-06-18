#include "ortools/sat/cp_model.h"
#include <iostream>
#include <vector>

using namespace operations_research;
using namespace std;
using namespace sat;

int main() {
    CpModelBuilder model;
   
    vector<int> profit = {8, 10, 6, 12};
    vector<int> cost = {3, 4, 2, 5};
    vector<BoolVar> x;
    
    for (int i = 0; i < profit.size(); i++) {
        x.push_back(model.NewBoolVar());  // x[i] ∈ {0,1}
    }

    LinearExpr totalP;
    LinearExpr totalProfit;

    for (int i = 0; i < x.size(); i++) {
        totalP += LinearExpr(x[i]) * cost[i];
        totalProfit += LinearExpr(x[i]) * profit[i];
    }

    model.AddLessOrEqual(totalP, 8);  // ∑ x[i] * cost[i] ≤ capacity
    model.Maximize(totalProfit); // max ∑ x[i] * profit[i]

    CpSolverResponse response = Solve(model.Build());

    cout << "Status: ";
    if (response.status() == CpSolverStatus::OPTIMAL) {cout << "Optimal \n";}
    else if (response.status() == CpSolverStatus::FEASIBLE) {cout << "Feasible \n";}
    else {cout << "Infeasible \n";}

    for (int i = 0; i < x.size(); i++) {
        cout << "Item " << i+1 << ": " << SolutionBooleanValue(response, x[i]) << endl;
    }
    
    cout << "Optimal Solution: " << response.objective_value();
    return 0;

}