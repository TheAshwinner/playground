/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <cmath>
#include <iostream>

// Notes:
// This seems to me to be a graph traversal problem with some paths
// that can be infinite length. So we would want a breadth-first
// approach here.
// Some things to watch out for:
// cycles: (9, 27) --> (27, 9) --> (9, 27) --> ...
//
// Approaches:
// If we have (x,y) with x = 0, we can immediately say that
// the path length will be the floor(log_3 y) + 1
// Can we use a heuristic to select the path that decreases xy the most?
// This might be a premature optimization though.
// This should just be straight breadth first search, nothing complicated.
//
// Actually.. I read the problem wrong. This isn't graph traversal at all.
// The solution should be to get the smallest number to 0 and then crush
// everything else down to 0.
// Edge cases: r = l+1
// Edge case: larger values
// Edge case: l=0

long long int log3floor(long long int num) { return floor(log(num) / log(3)); }

long long int computeNumOperationsToZero(long long int num) {
  return log3floor(num) + 1;
}

void ComputeMinOperations(long long int l, long long int r) {
  long long int operation_count = 0;
  // Bring the l to 0 and reset the other value
  operation_count += 2 * (computeNumOperationsToZero(l));

  // Determine how many powers of 3 lie in between (l+1, r) and which ones.
  // This will determine how long it takes each of the remaining numbers to
  // get crushed to 0.
  long long int left_pow3 = log3floor(l + 1);
  long long int right_pow3 = log3floor(r);
  for (long long int i = left_pow3; i <= right_pow3; ++i) {
    long long int left_num = (i == left_pow3) ? l + 1 : pow(3, i);
    long long int right_num = (i == right_pow3) ? r + 1 : pow(3, i + 1);
    operation_count +=
        (right_num - left_num) * computeNumOperationsToZero(pow(3, i));
  }
  std::cout << operation_count << "\n";
}

int main() {
  int t;
  std::cin >> t;

  for (int i = 0; i < t; ++i) {
    long long int l, r;
    std::cin >> l >> r;
    ComputeMinOperations(l, r);
  }
  return 0;
}