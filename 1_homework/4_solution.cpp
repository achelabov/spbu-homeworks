#include <iostream>
#include <math.h>

int main()
{
	int n;
	std::cin >> n;
	int x = sqrt(n+1);
	bool *is_prime = (bool*)malloc(sizeof(bool)*(n+1));
	
	for(int i = 2; i <= n; ++i)
	{
		is_prime[i] = true;
	}

	for(int i = 2; i <= x; ++i)
	{
		if(is_prime[i])
		{
			for(int j = i*i; j <= n; j+=i)
			{
				is_prime[j] = false;
			}
		}
	}

	for(int i = 2; i <= n; ++i)
	{
		if(is_prime[i])
		{
			std::cout << i << std::endl;
		}
	}

	free(is_prime);
	return EXIT_SUCCESS;
}
