#include <iostream>

namespace RUS {
    std::string greet() {
        return "ПРИВЕТ";
    }
}

namespace ENG {
    std::string greet() {
        return "HELLO";
    }
}

namespace ESP {
    std::string greet() {
        return "HOLA";
    }
}

int main() {
    std::cout << RUS::greet() << "\n";
    std::cout << ENG::greet() << "\n";
    std::cout << ESP::greet() << "\n";

    return 0;
}