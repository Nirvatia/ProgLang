#include <iostream>

float calc_avg(int a, int b) {
    return (a + b) / 2.0f;
}

int main() {
    decltype(calc_avg(10, 20)) res;

    res = calc_avg(10, 20);

    std::cout << res << std::endl;

    return 0;
}