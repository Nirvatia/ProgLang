#include <iostream>

int main()
{

    int x = 1;
    int y = 2;
    (++x) = y;

    std::cout << "x: " << x << ", " << "y: " << y << std::endl;

    return 0;
}