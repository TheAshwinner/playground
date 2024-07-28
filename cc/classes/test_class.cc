

#include "test_class.h"
#include <iostream>

namespace test_class {

void MyClass::set_string(std::string new_string) {
  myclass_string = new_string;
}

MyClass &MyClass::combine_strings(const MyClass &rhs) {
  set_string(myclass_string.append(rhs.get_string()));
  return *this;
}

std::string MyClass::get_string() const { return myclass_string; }

void MyClass::print_string() const { std::cout << myclass_string << std::endl; }

void Subclass::test_func() { std::cout << "Subclass test_func()\n"; }

void friend_function(const MyClass &my_class) {
  std::string new_string = my_class.myclass_string;
  std::cout << new_string << " friends\n";
  return;
}

void DoBar(MyClass myclass) {
  std::cout << myclass.get_string();
  repeated_func_in_header();
}

} // namespace test_class
