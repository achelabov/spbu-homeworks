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

bool isNatural(std::string str, int& index)
{
	if (isDigit(str[index]))
	{
		while (isDigit(str[++index]));

		return true;
	}
	return false;
}

bool isOrder(std::string str, int& index)
{
    if (str[index++] == 'E')
    {
        if (isNatural(str, index) || isSign(str[index++]) && isNatural(str, index))
        {
            return true;
        }
    }
    return false;
}

bool isMantissa(std::string str, int& index)
{
    if (str[index++] == '.' && isNatural(str, index))
    {
        return true;
    }
    return false;
}

bool isReal(std::string str, int& index)
{
    if (isMantissa(str, index) && isOrder(str, index) || isSign(str[index++]) && isMantissa(str, index) && isOrder(str, index)) 
    {
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
    
    int index = 0;
    if (isReal(str, index))
    {
        std::cout << "=)" << std::endl;
    }
    else
    {
        std::cout << "=(" << std::endl;
    }

    return 0;
}
