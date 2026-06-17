#include "ortools/sat/cp_model.h"
#include <vector>
#include <algorithm>
#include <iostream>

using namespace operations_research;
using namespace sat;
using namespace std;

int main () {
    CpModelBuilder model;
    
    int limit = 5;
    vector<int> value = {6, 10 ,6};
    vector<int> weight = {2, 3, 5};

    
    vector<BoolVar> x;
    for (int i = 0; i < value.size(); i ++ ){
        x.push_back(model.NewBoolVar());
    }
    
    LinearExpr weightT; 

    for (int i = 0; i < x.size(); i ++) {
        weightT += LinearExpr(x[i]) * weight[i];      // x.size() ∑ i = 1   x[i] * value[i] <= 5; 
    } 
    
    model.AddLessOrEqual(weightT, 5);
    model.AddEquality(LinearExpr(x[3]), 1);
    LinearExpr valueT;

    for (int i = 0; i < x.size(); i++) {
        valueT += LinearExpr(x[i]) * value[i]; 
    }

    model.Maximize(valueT);

    CpSolverResponse response = Solve(model.Build());
    
    cout << "Value: " << response.objective_value() << "\n";
    cout << "Items:";
    for (int i = 0; i < x.size(); i++) {
        cout << LinearExpr(x[i]) << " ";
    }
    return 0;
}