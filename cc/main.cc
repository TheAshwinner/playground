/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include "classes/class_util.cc"
#include "classes/class_util.h"
#include "classes/test_class.cc"
#include "classes/test_class.h"
#include "generic_programming/generic_programming.cc"
#include "testing/testing.cc"
#include <iostream>
using namespace std;

int main() {
  std::cout << "Hello world!" << endl;
  generic_programming::test_function();
  generic_programming::test_compare_template();
  testing::benchmarking_inline_function();

  test_class::MyClass my_class = test_class::MyClass("test");
  std::string test_string = "Original string";
  my_class.set_string(test_string);
  std::cout << "my_class.get_string(): " << my_class.get_string() << std::endl;

  test_class::MyClass my_class2 = test_class::MyClass("test2");
  my_class2.set_string("second class");
  std::cout << "my_class2.get_string(): " << my_class2.get_string()
            << std::endl;
  std::cout << "my_class.get_string(): " << my_class.get_string() << std::endl;
  const test_class::MyClass myclass_const = test_class::MyClass("test");
  myclass_const.get_string();

  test_class::MyClass my_class3 = my_class2.combine_strings(my_class);
  my_class3.print_string();
  my_class.print_string();
  test_class::friend_function(my_class);
  std::string believe_me = "believe_me";
  test_class::DoBar(believe_me);

  class_util::print_class(my_class);
  return 0;
}