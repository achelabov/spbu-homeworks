#include <iostream>

int main()
{
	int n = 0;
	int k = 1;
	std::cin >> n;
	int** a = new int* [n];
	for (int i = 0; i < n; ++i)
	{
		a[i] = new int[n + 1];
	}
	if(n % 2 != 0)
	{
	       	a[n / 2][n / 2] = n * n;
	}
	for(int i = 0; i < n / 2; i++)
	{
		for(int j = i; j < n - i; ++j)
		{
			a[i][j] = k;
			++k;
		}
		for(int j = 1; j < n - 2*i; ++j)
		{
			a[i + j][n - i - 1] = k;
			++k;
		}
		for(int j = n - i - 2; j >= i; j--)
		{
			a[n - i - 1][j] = k;
			++k;
		}
		for(int j = n - i - 2; j > i; j--)
		{
			a[j][i] = k;
			++k;
		}
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < n - 1; ++j)
		{
			std::cout << a[i][j] << " ";
		}
		std::cout << a[i][n - 1] << std::endl;
	}
	for (int i = 0; i < n; ++i)
	{
		delete[] a[i];
	}
	delete[] a;
	return EXIT_SUCCESS;
}
