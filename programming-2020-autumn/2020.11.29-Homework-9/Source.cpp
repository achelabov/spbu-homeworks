#include <iostream>
#include <string>

void resolveError(int errorCode)
{
	switch (errorCode)
	{
		case 0:
		{
			std::cout << "Введено неверное число" << std::endl;
			break;
		}
		case 1:
		{
			std::cout << "Слишком большое число" << std::endl;
			break;
		}
		case 2:
		{
			std::cout << "Double должен содержать \".\"" << std::endl;
		}
	}
}

short length(auto num)
{
	short count = 0;
	if (num < 0)
	{
		++count;
	}
	while (num)
	{
		num /= 10;
		++count;
	}
	return count;
}

long long getLongLong()
{
	std::string str;
	std::getline(std::cin, str);
	long long number;
	try
	{
		number = std::stoll(str);
	} catch (const std::invalid_argument& ia)
	{
		resolveError(0);
//		std::cout << ia.what() << std::endl;
		return getLongLong();
	} catch (const std::out_of_range& oor)
	{
		resolveError(1);
//		std::cout << oor.what() << std::endl;
		return getLongLong();
	}
	if (str.length() != length(number))
	{
		resolveError(0);
		return getLongLong();
	}
	return number;
}

auto pos(std::string& str)
{
	return str.find(".");
}

bool isPoint(std::string& str)
{
	return pos(str) != std::string::npos;
}

short doubleLength(std::string& str)
{
	std::string beforePoint;
	std::string afterPoint;
	if (isPoint(str))
	{
		beforePoint = str.substr(0, pos(str));
		afterPoint = str.substr(pos(str) + 1);
	}
	return length(std::stoi(beforePoint)) + length(std::stoi(afterPoint)) + 1;
}

double getDouble()
{
	std::string str;
	std::getline(std::cin, str);
	double number = 0;
	try
	{
		if (isPoint(str))
		{
			number = std::stod(str);
		} else
		{
			resolveError(2);
			return getDouble();
		}
	} catch (const std::invalid_argument& ia)
	{
		resolveError(0);
//		std::cout << ia.what() << std::endl;
		return getDouble();
	} catch (const std::out_of_range& oor)
	{
		resolveError(1);
//		std::cout << oor.what() << std::endl;
		return getDouble();
	}
	if (str.length() != doubleLength(str))
	{
		resolveError(0);
		return getDouble();
	}
	return number;
}

long double sum(long long ll, double d)
{
	return ll + d;
}

int main()
{
	std::cout << "Long long value: " << std::endl;
	long long ll = getLongLong();
	std::cout << "Double value: " << std::endl;
	double d = getDouble();
	std::cout << sum(ll, d) << std::endl;

	return EXIT_SUCCESS;
}
