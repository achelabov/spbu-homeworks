#include <iostream>
#include <set>
using namespace std;

template <class T>
set<T> fourth(set<T> s1, set<T> s2)
{

    set<T> res;
    res.insert(s1.begin(), s1.end());
    res.insert(s2.begin(), s2.end());
    
    return res;
}

void print(set<int> s)
{
    for (int x : s)
        cout << x << "  ";
    cout << endl;
}


int main()
{
    set<int> s1;
    set<int> s2;

    s1.insert(3);
    s1.insert(1);
    s1.insert(2);

    s2.insert(3);
    s2.insert(5);
    s2.insert(4);
    
    print(fourth(s1, s2));

    return EXIT_SUCCESS;
}

