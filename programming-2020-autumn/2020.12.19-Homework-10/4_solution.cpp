#include <iostream>

int main()
{
	int n = 0;
	std::cin >> n;
	int a[n][n];
	for (int i = 0; i < n; ++i)
	{
		for (int j = 1; j < n + 1; ++j)
		{
			if (i > j - 1)
			{
				a[i][j] = j;
			} 
			else
			{
				a[i][j] = i + 1;
			}
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
	return EXIT_SUCCESS;
}