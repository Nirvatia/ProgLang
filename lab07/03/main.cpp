#include <iostream>
#include <vector>

int main()
{
    std::vector<int> x(10);
    for (int i = 0; i < 10;)
        x[i++] = 1;

    for (int a : x)
    {
        std::cout << a << " ";
    }

    return 0;
}