#include <iostream>
#include <string>
#include <fstream>

bool isSign(char c)
{
    return c == '+' || c == '-';
}

bool isDigit(char c)
{
    return c >= '0' && c <= '9';
}

bool isNatural(string str, int& index)
{
	if (isDigit(str[index]))
	{
		while (isDigit(str[++index]));

		return true;
	}
	return false;
}

int main()
{
    std::string str;

    std::ifstream fin("in.txt");
    if (fin.is_open())
    {
        getline(fin, str);
    }
    fin.close();

    return 0;
}
