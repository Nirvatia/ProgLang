#include <iostream>

int main()
{
    bool x = true, y = false;
    auto a = x & y;
    std::cout << "Тип a " << typeid(a).name() << std::endl;
    auto b = x && y;
    std::cout << "Тип b " << typeid(b).name() << std::endl;
}