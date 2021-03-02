#include <iostream>
#include <string>
#include <cmath>
#include <cassert>

template<class T1, class T2>
T1 sum(T1 a, T2 b)
{
	return a + b;
}

template<class T1, class T2>
T1 diff(T1 a, T2 b)
{
	return a - b;
}

template<class T1, class T2>
T1 mult(T1 a, T2 b)
{
	return a * b;
}

template<class T1, class T2>
T1 div(T1 a, T2 b)
{
	return b == 0 ? -1 : a / b;
}

template<class T1, class T2>
T1 mod(T1 a, T2 b)
{
	return fmod(a, b);
}

int operationIndex(char op)
{
	switch (op)
	{
		case '+':
			return 0;
		case '-':
			return 1;
		case '*':
			return 2;
		case '/':
			return 3;
		case '%':
			return 4;
		default:
			return -1;
	}
}

template<class T1, class T2>
T1 calc(T1 a,T2 b, char op)
{
	T1(*operations[5])(T1, T2) = { sum, diff, mult, div, mod};
	return operations[operationIndex(op)](a, b);
}

void check(int argc, char** argv)
{
	assert(argc == 7 && "wrong number of parameters");
	assert(std::string(argv[1]) == "--operand1" && std::string(argv[3]) == "--operand2" && 
	       std::string(argv[5]) == "--operator" && "parameters entered incorrectly");
}

int main(int argc, char** argv)
{
	check(argc, argv);
	
	std::cout << calc(std::stod(argv[2]), std::stod(argv[4]), *argv[6]);	
	
	return 0;
}
