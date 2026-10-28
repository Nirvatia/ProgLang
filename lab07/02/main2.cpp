#include <iostream>

int main()
{
    int x = 1;
    int y = 2;
    int z = 3;

    x = x + 1, z = z + 2 * x + 3 * y, y = y + 1;

    std::cout << "x: " << x << ", " << "y: " << y << ", " << "z: " << z << std::endl;

    return 0;
}