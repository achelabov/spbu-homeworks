#include <iostream>
#include <math.h>

bool is_prime(int n)
{
	for(int i = 2; i <= sqrt(n); ++i)
	{
		if(n % i == 0)
		{
			return false;
		}
	}
	return true;
}

void func(int n)
{
	for(int i = 2; i <= n; ++i)
	{
		if(is_prime(i))
		{
			std::cout << i << std::endl;
		}
	}
}

int main()
{
	int n;
	std::cin >> n;
	func(n);
	return EXIT_SUCCESS;
}
