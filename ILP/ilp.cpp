#include "ortools/sat/cp_model.h"
#include <vector>
#include <algorithm>

using namespace operations_research;
using namespace sat;
using namespace std;

int main () {
    CpModelBuilder model;
    
    int limit = 5;
    vector<int> value = {6, 10 ,6};
    vector<int> weight = {2, 3, 5};

    
    BoolVar x1 = model.NewBoolVar();
    BoolVar x2 = model.NewBoolVar();
    BoolVar x3 = model.NewBoolVar();
    
    
    model.Add(x1 * weight[0] + x2 * weight[1] + x3 * weight[2] <= limit);

    
    
    model.Maximize(x1 * value[0] + x2 * value[1] + x3 * value[2]);


    CpSolver solver;
    const CpSolverResponse response = Solve(model.Build());

    return 0;
}