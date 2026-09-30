#include <iostream>

int main() {
    int x = 2;
    int y = 1;
    int z = 2;

    std::cout << ((x == y) + (x == z) == true) << std::endl;
}