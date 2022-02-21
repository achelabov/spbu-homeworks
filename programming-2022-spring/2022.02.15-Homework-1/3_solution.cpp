#include <iostream>
#include <set>
using namespace std;

int main()
{
    set<int> s;
    set<int> recurring;
    set<int> recurring2;
    int add;
    while (cin.good())
    {
        cin >> add;

        if (s.count(add))
        {
            if (!recurring.count(add))
                recurring2.insert(add);

            recurring.insert(add);
        }
        s.insert(add);
    }

    for (int x : recurring2)
        cout << x << "  ";
    cout << endl;

}
