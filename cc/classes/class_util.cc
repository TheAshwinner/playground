#include "test_class.h"
#include <iostream>

namespace class_util {
void print_class(test_class::MyClass &myclass) {
  std::cout << "\nTest\n";
  repeated_func_in_header();
}
} // namespace class_util