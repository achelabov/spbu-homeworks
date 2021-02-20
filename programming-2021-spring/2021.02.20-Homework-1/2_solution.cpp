#include <iostream>
#include <stdarg.h>

double average(int n, ...)
{
	va_list valist;
	double sum = 0.0;
	va_start(valist, n);

	for (int i = 0; i < n; ++i)
	{
		sum += va_arg(valist, int);
	}

	va_end(valist);

	return sum/n;
}

int main()
{
	std::cout << average(4, 3, 7, 12, 21);

	return 0;
}
