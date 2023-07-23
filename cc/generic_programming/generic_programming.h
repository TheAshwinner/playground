
#ifndef GENERIC_PROGRAMMING_H
#define GENERIC_PROGRAMMING_H

namespace generic_programming {
void test_function();

template <typename T>
int compare(const T& v1, const T& v2) {
    if (v1 < v2) return -1;
    if (v2 < v1) return 1;
    return 0;
}

void test_compare_template();
}

#endif