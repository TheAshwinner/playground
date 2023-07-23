
#include "generic_programming.h"
#include <iostream>
using namespace std;

namespace generic_programming {
void test_function() {
    std::cout << "test_function() in generic_programming namespace." << endl;
}

void test_compare_template(){
    std::cout << "v1: " << 4 << ", v2: " << 7 << ", compare: " <<
        compare(4,7) << endl;
    std::string string1 = "banana";
    std::string string2 = "cabbage";
    std::cout << "v1: " << "banana" << ", v2: " << "cabbage" << ", compare: " <<
        compare(string1, string2) << endl;
}



}