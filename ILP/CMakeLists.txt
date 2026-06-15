cmake_minimum_required(VERSION 3.20)
project(ilp_demo)

set(CMAKE_CXX_STANDARD 17)

find_package(ortools CONFIG REQUIRED)

add_executable(ilp ilp.cpp)
target_link_libraries(ilp ortools::ortools)
