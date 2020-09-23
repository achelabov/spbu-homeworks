#include <iostream>

int main()
{
	int result, n;
	std::cin >> n;
	result = 1 << n;
	std::cout << result <<std::endl;
	return EXIT_SUCCESS;
}
