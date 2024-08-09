/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <iostream>
#include <vector>
using namespace std;

long long int Factorial(long long int num) {
  if (num == 1) {
    return 1;
  } else {
    return num * Factorial(num - 1);
  }
}

int main() {
  long long int m, n;
  cin >> m >> n;
  cout << Factorial(std::min(m, n)) << "\n";

  return 0;
}