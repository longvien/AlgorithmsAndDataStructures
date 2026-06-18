#include "ortools/sat/cp_model.h"
#include <vector>
#include <iostream>

using namespace operations_research;
using namespace sat;
using namespace std;

int main () {
    CpModelBuilder model;

    vector<int> value = {6, 10 ,6};
    vector<int> weight = {2, 3, 5};
    
    vector<BoolVar> x;
    for (int i = 0; i < value.size(); i ++ ){
        x.push_back(model.NewBoolVar());
    }
    
    LinearExpr weightT; 
    LinearExpr valueT;

    for (int i = 0; i < x.size(); i ++) {
        weightT += LinearExpr(x[i]) * weight[i];      // ∑ x[i] * value[i] <= 5
        valueT += LinearExpr(x[i]) * value[i]; 
    } 
    
    model.AddLessOrEqual(weightT, 5);
    model.Maximize(valueT);

    CpSolverResponse response = Solve(model.Build());
    
    cout << "Value: " << response.objective_value() << "\n";
    
    for (int i = 0; i < x.size(); i++) {
        cout << "Items: "<< i + 1 << ": " << SolutionBooleanValue(response, x[i]) << endl;
    }
    return 0;
}