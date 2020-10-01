#include <iostream>

int factorial(int n)
{
	return n <= 1 ? 1 : n * factorial(n-1);
}

int main()
{
	int n;
	std::cin >> n;
	std::cout << factorial(n) << std::endl;
	return EXIT_SUCCESS;
}
