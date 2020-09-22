#include <iostream>

int main()
{
	int n;
	std::cin >> n;
	std::cout << n*(n*(n*(n+1)+1)+1)+1 << std::endl;
	return EXIT_SUCCESS;
}
