#include <iostream>
#include <map>
using namespace std;

map<int,int> foo ()
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

    for (auto x : m)
        cout << x.first << " -> " << x.second << endl;

    return EXIT_SUCCESS;
}
