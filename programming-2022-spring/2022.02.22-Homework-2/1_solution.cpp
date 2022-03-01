#include <iostream>
#include <map>
using namespace std;

int main()
{
    map<int, int> m;

    int add;

    while (cin >> add)
    {
        ++m[add];
    }

    for (auto x : m)
        cout << x.first << "->" << x.second << endl;

    return EXIT_SUCCESS;
}
