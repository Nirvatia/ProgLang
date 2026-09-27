#include <iostream>
#include <vector>

typedef std::vector<int> Numbers;

int main() {
    Numbers my_numbers = {1, 2, 3};

    std::cout << my_numbers.size() << std::endl;
    
    return 0;
}