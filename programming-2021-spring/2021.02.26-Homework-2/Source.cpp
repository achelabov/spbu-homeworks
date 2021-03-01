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

template<class T1, class T2>
void calc(T1 a,T2 b, T1 (*op)(T1, T2))
{
	std::cout << op(a, b) << std::endl;
}

template<class T1, class T2>
void resolveOpNumber(T1 operand1, T2 operand2, char op)
{
	switch (op)
	{
		case '+':
		{
			calc(operand1, operand2, sum);
			break;
		}
		case '-':
		{
			calc(operand1, operand2, diff);
			break;
		}
		case '*':
		{
			calc(operand1, operand2, mult);
			break;
		}
		case '/':
		{
			calc(operand1, operand2, div);
			break;
		}
		case '%':
		{
			calc(operand1, operand2, mod);
			break;
		}
	}
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

	resolveOpNumber(std::stod(argv[2]), std::stod(argv[4]), *argv[6]);
	
	return 0;
}
