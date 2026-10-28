#include <iostream>

int main()
{
    int x = 1;
    int y = 2;
    int z = 3;

    z += 2 * (x += 1) + 3 * y, y += 1;

    std::cout << "x: " << x << ", " << "y: " << y << ", " << "z: " << z << std::endl;

    return 0;
}