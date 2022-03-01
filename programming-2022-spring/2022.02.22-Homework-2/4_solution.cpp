#include <iostream>
#include <map>
using namespace std;

template <class T1, class T2>
map<T1, T2> sum(map<T1,T2> m1, map<T1,T2> m2)
{
    map<T1,T2> res;
    for (auto x : m1)
        res.insert(pair<T1,T2>(x.first, m1[x.first] + m2[x.first]));

    return res;
}

int main()
{
    map<int,int> m1, m2, m;
    m1[1] = 2;
    m1[2] = 3;
    m2[1] = 4;
    m2[2] = 7;
    
    m = sum(m1, m2);

    for (auto x : m)
        cout << x.first << " -> " << x.second << endl;

    return EXIT_SUCCESS;
}
