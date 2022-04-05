#include <iostream>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <omp.h>
using namespace std;

struct Point
{
    float x, y, z;
    Point(float x, float y, float z) : x(x), y(y), z(z) {};
};

float dist(Point p1, Point p2)
{
    return sqrt((p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) *
                (p1.y - p2.y) + (p1.z - p2.z) * (p1.z - p2.z));
}

float successively(vector<Point> vect)
{
    double t = omp_get_wtime();
    float max = 0;
    for (int i = 0; i <  vect.size() - 1; ++i)
    {
        for (int j = i + 1; j < vect.size(); ++j)
        {
            if (dist(vect[i], vect[j]) > max)
                max = dist(vect[i], vect[j]);
        }
    }
    cout << "time succ: " << omp_get_wtime() - t << endl;
    return max;
}

float parallel(vector<Point> vect)
{
    double t = omp_get_wtime();
    float m = 0;
#pragma omp parallel for schedule(static, 5) reduction(max:m) 
    for (int i = 0; i <  vect.size() - 1; ++i)
    {
        for (int j = i + 1; j < vect.size(); ++j)
        {
            if (dist(vect[i], vect[j]) > m)
                m = dist(vect[i], vect[j]);
        }
    }
    cout << "time parallel: " << omp_get_wtime() - t << endl;
    return m;
}

int main()
{
    Point p1(1.2, 2.3, 3.4); 
    Point p2(2.2, 5.3, 4.4);
    Point p3(1.2, 3.3, 5.4);
    Point p4(5.2, 2.3, 3.4);
    vector<Point> vect {p1, p2, p3, p4}; 

    cout << successively(vect) << endl;
    cout << parallel(vect) << endl;
    return EXIT_SUCCESS;
}
