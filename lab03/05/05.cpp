#include <iostream>

struct Enemy {
    int id;
    char tier;
};

int main() {
    std::cout << sizeof(Enemy) << std::endl;

    return 0;
}