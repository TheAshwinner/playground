#ifndef TEST_CLASS_H
#define TEST_CLASS_H

#include <iostream>
#include <string>

namespace test_class {

class MyClass {
  friend void friend_function(const MyClass &my_class);

public:
  typedef std::string pos;
  MyClass() : MyClass("Fake") {}
  MyClass(std::string new_string) : myclass_string(new_string) {}
  void set_string(std::string new_string);
  std::string get_string() const;
  MyClass &combine_strings(const MyClass &rhs);
  void print_string() const;

private:
  std::string myclass_string;
};

class AbstractClass {
public:
  virtual void test_func() = 0;
};

class Subclass : AbstractClass {
public:
  void test_func() override;
};

void friend_function(const MyClass &my_class);
void DoBar(MyClass myclass);
} // namespace test_class

void repeated_func_in_header() { std::cout << "repeated_func_in_header\n"; }

#endif // TEST_CLASS_H