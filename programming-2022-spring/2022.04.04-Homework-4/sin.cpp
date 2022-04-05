#include <iostream>
#include <cstdlib>
#include <cmath>
#include <omp.h>
using namespace std;

double* sin_c = new double[10000000];
double* sin_p = new double[10000000];

void sin_successively(int n)
{
	double t = omp_get_wtime();
	for (int i = 0; i <= n; ++i)
	{
		sin_c[i] = sin(M_PI * i / (2 * n));
	}
    cout << "omp_get_wtime: " << omp_get_wtime() - t << endl;
}

void sin_parallel(int n)
{
/*
	double t = omp_get_wtime();
#pragma omp parallel for schedule(static, 5)
		for (int i = 0; i <= n; ++i)
		{
			sin_p[i] = sin(M_PI * i / (2 * n));
		}
	cout << "time static: " << omp_get_wtime() - t << endl;
*/
	double t1 = omp_get_wtime();
#pragma omp parallel for schedule(dynamic, 7)
		for (int i = 0; i <= n; ++i)
		{
			sin_p[i] = sin(M_PI * i / (2 * n));
		}
	cout << "time dinamic: " << omp_get_wtime() - t1 << endl;
/*
	double t2 = omp_get_wtime();
#pragma omp parallel for schedule(guided, 5)
		for (int i = 0; i <= n; ++i)
		{
			sin_p[i] = sin(M_PI * i / (2 * n));
		}
	cout << "time guided: " << omp_get_wtime() - t2 << endl;
*/
}

int main()
{
    int n;
    cin >> n;
    sin_successively(n);
    sin_parallel(n);

    return EXIT_SUCCESS;
}
