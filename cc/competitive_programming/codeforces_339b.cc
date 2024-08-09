/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <iostream>
#include <vector>
using namespace std;

int main() {
  int m, n;
  cin >> n >> m;
  std::vector<int> task_houses;
  for (int k = 0; k < m; ++k) {
    int task;
    cin >> task;
    task_houses.push_back(task);
  }
  long long int running_count = 0;
  int current_house = 1;

  for (int i = 0; i < task_houses.size(); ++i) {
    if (task_houses[i] >= current_house) {
      running_count += task_houses[i] - current_house;
      current_house = task_houses[i];
    } else {
      running_count += (n - current_house) + task_houses[i];
      current_house = task_houses[i];
    }
  }

  std::cout << running_count << "\n";

  return 0;
}