#include <iostream>

int main()
{
	int n;
	std::cin >> n;
	unsigned int result = 0;
	int num = 11111;
   	for (unsigned int i = 1; num; num/=10, i*=n)
	{
        	result += i*(num%10);
    	}
	std::cout << result << std::endl;
	return EXIT_SUCCESS;
}
