#include <iostream>
#include <vector>

int main() {
    std::vector<double> prices = {10.5, 20.1, 30.0};

    for (auto price : prices) {
        std::cout << price << " ";
    }
    
    std::cout << std::endl;

    return 0;
}