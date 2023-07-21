/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <iostream>
#include "generic_programming/generic_programming.cc"
#include "testing/testing.cc"
using namespace std;

int main() {
    std::cout << "Hello world!" << endl;
    generic_programming::test_function();
    testing::benchmarking_inline_function();
    return 0;
}