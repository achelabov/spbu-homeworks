#include <iostream>

int main()
{
	unsigned int result, n;
	std::cin >> n;
	result = ~0;
	result = result << n;
	result = ~result;
	std::cout << result << std::endl;
	return EXIT_SUCCESS;
}
