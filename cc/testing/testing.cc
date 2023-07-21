
#include <iostream>
#include <chrono>

using namespace std::chrono;

namespace testing {
void test_function() {
    std::cout << "test_function() is working." << std::endl;
}

void small_function1() {
    std::cout << "small_function1() is running." << std::endl;
}

inline void small_function2() {
    std::cout << "small_function2() is running inline." << std::endl;    
}

// The point of this function is to test out if inline functions
// actually speed up the program.
void benchmarking_inline_function() {
    steady_clock::time_point start_time = high_resolution_clock::now();
    small_function1();
    steady_clock::time_point mid_time = high_resolution_clock::now();
    small_function2();
    steady_clock::time_point end_time = high_resolution_clock::now();

    // It seems that in practice, the non-inline took 3 microseconds
    // with the inline taking 2 microseconds.
    // Unsure if this is correctly benchmarked
    std::cout << "Non-inline function: " << duration_cast<microseconds>(
        mid_time - start_time).count() << std::endl;
    std::cout << "Inline function: " << duration_cast<microseconds>(
        end_time - mid_time).count() << std::endl;
}
}