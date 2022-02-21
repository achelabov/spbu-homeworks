#include <iostream>
#include <set>
using namespace std;

void first(set<int> s)
{
    for (int x : s)
        cout << x << "  ";
    cout << endl;
}

int main()
{
    set<int> s; 
    int add;
    while (cin.good())
    {
        cin >> add;
        s.insert(add);
    }
    first();

    return EXIT_SUCCESS;
}
