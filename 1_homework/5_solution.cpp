#include <iostream>

int count_of_divisors(int n)
{
    int res = 0;

    for (int i = 2; i * i <= n; ++i)
        if (n % i == 0)
            res += 2 - (i *i == n);

    return res + 2 - (n == 1);
}

int main()
{
        int num;
        std::cin >> num;

        std::cout << count_of_divisors(num) << std::endl;
        return EXIT_SUCCESS;
}
 
