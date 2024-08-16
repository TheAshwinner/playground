/**
Usage:
g++ -o main.o cc/main.cc
./main.o
*/

#include <iostream>
// Edge cases:
// empty string s, t
// t is same length or larger than s
// all question marks
// t finishes early
// They both finish at the same time
// s finishes first

void CanBeSubsequence(std::string s, std::string t) {
  int s_i, t_i = 0;
  std::string valid_string;
  while (s_i < s.length() && t_i < t.length()) {
    if (s[s_i] == t[t_i] || s[s_i] == '?') {
      valid_string += t[t_i];
      s_i += 1;
      t_i += 1;
    } else {
      // This should never be "?"
      valid_string += s[s_i];
      s_i += 1;
    }
  }
  if (t_i >= t.length()) {
    // We found a substring so now we need to go through the rest of s to add it
    // to valid string
    while (s_i < s.length()) {
      if (s[s_i] != '?') {
        valid_string += s[s_i];
      } else {
        valid_string += "a";
      }
      s_i += 1;
    }
    std::cout << "YES\n";
    std::cout << valid_string << "\n";
  } else {
    std::cout << "NO\n";
  }
}

int main() {
  int t;
  std::cin >> t;

  for (int i = 0; i < t; ++i) {
    std::string s, t;
    std::cin >> s;
    std::cin >> t;
    CanBeSubsequence(s, t);
  }

  return 0;
}