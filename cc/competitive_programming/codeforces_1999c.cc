/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>

// List of possible edge cases:
// No open interval at the start
// No open interval at the end
// A single time slot that takes up the entire time
// No time slots so the entire time is available
// One time slot starting right when the previous one ends
// We can assume l < r

void computeTestCase() {
  long long int n, s, m;
  std::cin >> n >> s >> m;

  std::vector<std::tuple<long long int, long long int>> intervals;
  for (int j = 0; j < n; ++j) {
    long long int x, y;
    std::cin >> x >> y;
    intervals.push_back(std::make_tuple(x, y));
  }
  std::sort(intervals.begin(), intervals.end());

  // Alex has no tasks planned for today.
  if (intervals.empty()) {
    if (m >= s) {
      std::cout << "YES\n";
    } else {
      std::cout << "NO\n";
    }
    return;
  }

  // Alex has free time when his day starts.
  if (std::get<0>(intervals[0]) >= s) {
    std::cout << "YES\n";
    return;
  }

  // Alex has free time in between planned activities
  for (int k = 0; k < intervals.size() - 1; ++k) {
    if (std::get<0>(intervals[k + 1]) - std::get<1>(intervals[k]) >= s) {
      std::cout << "YES\n";
      return;
    }
  }

  // Alex has free time at the end of his day.
  if (m - std::get<1>(intervals[intervals.size() - 1]) >= s) {
    std::cout << "YES\n";
    return;
  }

  std::cout << "NO\n";
}

int main() {
  int t;
  std::cin >> t;

  for (int i = 0; i < t; ++i) {
    computeTestCase();
  }

  return 0;
}