#include <iostream>
#include <map>
using namespace std;

template <class T1, class T2, class T3>
map<T1,T3> mapping(map<T1,T2> m1, map<T2,T3> m2)
{
    map<T1,T3> m;
    for (auto x : m1)
        if (m2.count(x.second))
             m[x.first] = m2[x.second];

    return m;
}

int main()
{
    map<int,int> m1, m2, m;
    m1[1] = 'q';
    m1[2] = 'w';
    m2['q'] = 4;
    m2['w'] = 7;
    
    m = mapping(m1, m2);

    for (auto x : m)
        cout << x.first << " -> " << x.second << endl;;

    return EXIT_SUCCESS;
}
