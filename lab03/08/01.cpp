#include <iostream>

int main() {
    int x = 1;
    int y = 1;
    int z = 2;

    std::cout << ((x == y) + (x == z) == true) << std::endl;
}