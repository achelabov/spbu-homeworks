#include <iostream>

template<typename T>
void printBits(T a)
{
	int x = 0;
	for (int i = sizeof(a) * 8 - 1; i >= 0; --i)
	{
		x = ((a >> i) & 1);
		std::cout << x;
	}
}

int main()
{
	printBits(20022021);
	return 0;
}
