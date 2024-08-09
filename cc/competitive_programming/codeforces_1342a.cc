/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    long long int x, y, a, b;
    cin >> x >> y;
    cin >> a >> b;

    // if (x >= 0 && y >= 0) {
    //     cout << std::min(x,y) * b + abs(x-y) * a;
    // } else if (x <= 0 && y <= 0) {
    //     x = abs(x);
    //     y = abs(x);
    //     cout << std::min(x,y) * b + abs(x-y) * a;
    // } else {
    //     cout << abs(x-y)*a;
    // }
    cout << abs(x - y) * a +
                std::min(std::min(x, y) * b, 2 * std::min(x, y) * a)
         << "\n";
  }

  return 0;
}