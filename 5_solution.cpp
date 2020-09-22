#include <iostream>

int count(int n)
{
	int c = 0;
	for(int i = 1; i <= n; ++i)
	{
		if(n % i == 0)
		{
			c++;
		}
	}
	return c;
}

int main()
{
	int n;
	std::cin >> n;
	std::cout << count(n) << std::endl;
	return EXIT_SUCCESS;
}
