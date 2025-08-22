#include <iostream>
int main() {
    std::cout << "¡Hola, mundo!" << std::endl;
    int edad; 
    std::cout << "Introduce tu edad: ";
    std::cin >> edad;
    std::cout << "Tienes " << edad << " años." << std::endl;
    return 0;
}




#include <iostream>
int main() {
    std::cout << "¡Hola, mundo!" << std::endl;
    float edad; 
    std::cout << "Introduce tu edad: ";
    std::cin >> edad;
    std::cout << "Tienes " << edad << " años." << std::endl;
    char letra = 'A';
    std::cout << "Char: " << letra << std::endl;
    return 0;
}


#include <iostream>
int main() {
    std::cout << "¡Hola, mundo!" << std::endl;
    int edad; 
    std::cout << "Introduce tu edad: ";
    std::cin >> edad;
    std::cout << "Tienes " << edad << " años." << std::endl;
    int xd ;
    std::cout << " estas seguro ? si o no ";
    std::cin << xd;
    std::cout << "estas seguro " << xd << " tu edad es " << edad << std::endl;
    return 0;
}




#include <iostream>
int main() {
    int edad;
    std::cout << "Introduce tu edad: ";
    std::cin >> edad;
    if (edad < 18) {
        std::cout << "Eres menor de edad no puede hacer nada jijiji." << std::endl;
    } else if (edad >= 18 && edad <= 55) {
        std::cout << "Eres un adulto bobo." << std::endl;
    } else {
        std::cout << "Eres un anciano jijiji." << std::endl;
    }
    return 0;
}