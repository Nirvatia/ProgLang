#include <iostream>

int main() {
    int total = 9;
    int cnt = 2;

    double avg = static_cast<double>(total) / cnt;

    std::cout << avg << std::endl;

    return 0;
}