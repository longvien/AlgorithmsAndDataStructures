cmake_minimum_required(VERSION 3.20)
project(ilp_demo)

set(CMAKE_CXX_STANDARD 17)

find_package(ortools CONFIG REQUIRED)

add_executable(ilpBasicSyntax ilpBasicSyntax.cpp)
target_link_libraries(ilpBasicSyntax ortools::ortools)

add_executable(knapsack knapsack.cpp)
target_link_libraries(knapsack ortools::ortools)