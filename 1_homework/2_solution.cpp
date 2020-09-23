#include <iostream>

int division(int a, int b)
{
	int count = 0;
	int num = b;
	while(a >= num)
	{
		num+=b;
		count+=1;
	}
	return count;
}

int main()
{
	int a, b;
	std::cin >> a >> b;
	std::cout << division(a, b) << std::endl;
	return EXIT_SUCCESS;
}
