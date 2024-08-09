/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <iostream>
using namespace std;

bool DoesSumeetWin(int a1, int a2, int b1, int b2) {
  // a1 plays b1, a2 plays b2
  int count = 0;
  if (a1 > b1) {
    count += 1;
  } else if (a1 < b1) {
    count -= 1;
  }

  if (a2 > b2) {
    count += 1;
  } else if (a2 < b2) {
    count -= 1;
  }

  return count > 0;
}

int main() {
  int t;
  cin >> t;

  for (int i = 0; i < t; ++i) {
    int a1, a2, b1, b2;
    cin >> a1 >> a2 >> b1 >> b2;

    int win_count =
        (DoesSumeetWin(a1, a2, b1, b2) + DoesSumeetWin(a2, a1, b1, b2)) * 2;
    cout << win_count << "\n";
  }

  return 0;
}