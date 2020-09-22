#include <iostream>
//#include <math.h>

int func(int a, int b)
{
	int num = a;
	while(b > 1)
	{
		num*=a;
		b--;
	}
	return num;
}

int main()
{
	int a,b;
	std::cin >> a >> b;
//	std::cout << pow(a,b) << std::endl;
	std::cout << func(a,b) << std::endl;
	return EXIT_SUCCESS;
}

