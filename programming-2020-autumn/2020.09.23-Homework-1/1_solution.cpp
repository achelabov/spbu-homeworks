#include <iostream>

int main()
{
	int n;
	std::cin >> n;
	int square = n*n;
	int result = (square + n) * (square +1) + 1;
	std::cout << result << std::endl;
	return EXIT_SUCCESS;
}
