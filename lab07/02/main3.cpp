#include <iostream>

int main()
{
    int x = 1;
    int y = 2;
    int z = 3;

    z = z + 2 * (++x) + 3 * (y++);

    std::cout << "x: " << x << ", " << "y: " << y << ", " << "z: " << z << std::endl;

    return 0;
}