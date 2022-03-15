#include <iostream>
#include <cstdlib>
#include <cmath>
#include <omp.h>
using namespace std;

double function(double x)
{
    return (1 / (1 + x * x));
}

double pi_successively(int n)
{
    double t = omp_get_wtime();
    double sum = 0;
    for (int i = 1; i <= n; ++i)
    {
        sum += function((2 * i - 1) / (2 * n));
    }
    cout << "omp_get_wtime: "  << omp_get_wtime() - t<< endl; 

    return 4 * sum / n;
}

double pi_parallel(int n)
{
	double t = omp_get_wtime();
    double sum = 0;
#pragma omp parallel sections reduction(+:sum)
	{
#pragma omp section
		{
			for (int i = 1; i < n / 2; i++)
			{
                sum += function((2 * i - 1) / (2 * n));
			}
		}
#pragma omp section
		{
			for (int i = n / 2; i <= n; i++)
			{
                sum += function((2 * i - 1) / (2 * n));
			}
		}
	}
	cout << "omp_get_wtime parallel: " << omp_get_wtime() - t<< endl;

    return 4 * sum / n;
}

int main()
{
    int n;
    cin >> n;
    cout << pi_successively(n) << endl;
    cout << pi_parallel(n) << endl;

    return EXIT_SUCCESS;
}
