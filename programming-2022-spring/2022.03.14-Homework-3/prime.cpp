#include <iostream>
#include <cstdlib>
#include <cmath>
#include <omp.h>
using namespace std;

bool prime(int n)
{
    if (n == 1) return false;
    if (n % 2 == 0 && n != 2)
        return false;

    for (int i = 3; i * i <= n; i += 2)
        if (n % i == 0)
            return false;

    return true; 
}

int prime_numbers_successively(int n)
{
    double t = omp_get_wtime();
    int count = 0;
    for (int i = 3; i <= n; i += 2)
        count += prime(i);
    cout << "omp_get_wtime: " << omp_get_wtime() - t << endl;
    return count;
}

int prime_numbers_parallel(int n)
{
    double t = omp_get_wtime();
    int count = 0;
#pragma omp parallel sections reduction(+:count)
{
#pragma omp section
    {
        for (int i = 3; i <= n; i += 4)
            count += prime(i);
    }

#pragma omp section
   {
        for (int i = 5; i <= n; i += 4)
            count += prime(i);
    }
}
    cout << "omp_get_wtime parallel: " << omp_get_wtime() - t << endl;
    return count;
}

int main()
{
    int n;
    cin >> n;
    cout << prime_numbers_successively(n) << endl;
    cout << prime_numbers_parallel(n) << endl;
    return EXIT_SUCCESS;
}
