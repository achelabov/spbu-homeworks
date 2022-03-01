#include <iostream>
#include <map>
using namespace std;

map<int,int> foo()
{
    map<int,int> m;
    int key, value, cnt;
    cin >> cnt;

    while (cnt)
    {
        cin >> key >> value;
        m.insert(pair<int,int>(key, value));
        --cnt;
    }
    return m;
}

int main()
{
    map<int,int> m = foo();
    int add;

    while (cin >> add)
    {
        if (m.count(add))
        {
            cout << m[add] << endl;
        } else
        {
            cout << add << endl;
        }
    }

    return EXIT_SUCCESS;
}
