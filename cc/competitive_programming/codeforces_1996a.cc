/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <iostream>
using namespace std;

int computeMinAnimalCount(int legs_count) {
  int cow_count = legs_count / 4;
  int chicken_count = (legs_count - 4 * cow_count) / 2;
  return cow_count + chicken_count;
}

int main() {
  int test_case_count;
  int current_leg_count;
  cin >> test_case_count;
  for (int i = 0; i < test_case_count; ++i) {
    cin >> current_leg_count;
    std::cout << computeMinAnimalCount(current_leg_count) << "\n";
  }
  return 0;
}