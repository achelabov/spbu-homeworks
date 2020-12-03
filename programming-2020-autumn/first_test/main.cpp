#include <iostream>
#include <cmath>
#include <iomanip>

double taylor(double x, int n)
{
	double precision = 1;
	double tmp = x;
	double result = 1;
	for (int i = 0; i < n; ++i)
	{
		precision *= 0.1;
	}/*
	for (int i = 0; abs(tmp) >= precision; ++i)
	{
		tmp = pow(x, i);
		result += tmp;
	}*/
	while (abs(x) >= precision)
	{
		result += x;
		x *= tmp;
	}
	return result;
}

int main()
{
	double x = 0;
	int n = 0;
	std::cin >> x >> n;

	std::cout << "C++: " << std::setprecision(9) << 1 / (1 - x) << std::endl;
	std::cout << "taylor: " << std::setprecision(9) << taylor(x, n) << std::endl;

	return EXIT_SUCCESS;
}
