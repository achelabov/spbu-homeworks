#include <iostream>

int main()
{
	int n = 0;
	std::cin >> n;
	int** a = new int* [n];
	for (int i = 0; i < n; ++i)
	{
		a[i] = new int[n + 1];
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 1; j < n + 1; ++j)
		{
			a[i][j] = i + j;
		}
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 1; j < n + 1; ++j)
		{
			std::cout << a[i][j] << " ";
		}
		std::cout << std::endl;
	}
	for (int i = 0; i < n; ++i)
	{
		delete[] a[i];
	}
	delete[] a;
	return EXIT_SUCCESS;
}
