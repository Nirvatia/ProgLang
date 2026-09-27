#include <iostream>

int main() {
    int a = 1;
    int b = 2;
    int c = 3;

    if ((a == b) + c) {
        std::cout << "OK" << std::endl;
    } else {
        std::cout << "NOT OK" << std::endl;
    }
}