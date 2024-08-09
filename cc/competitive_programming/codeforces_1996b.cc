/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <iostream>
#include <vector>
using namespace std;

void scaleCell() {
  int n, k;
  cin >> n >> k;

  std::vector<std::string> square;
  for (int row = 0; row < n; ++row) {
    std::string curr_row;
    cin >> curr_row;
    square.push_back(curr_row);
  }

  for (int i = 0; i < n; i += k) {
    for (int j = 0; j < n; j += k) {
      cout << square[i][j];
    }
    cout << "\n";
  }
}

int main() {
  int test_case_count;
  cin >> test_case_count;
  for (int i = 0; i < test_case_count; ++i) {
    scaleCell();
  }

  return 0;
}