#include <iostream>
#include <set>
using namespace std;

int main()
{
    set<int> s; 
    set<int> recurring;
    int add;
    while (cin.good())
    {
        cin >> add;
        
        if (s.count(add))
            recurring.insert(add);
        s.insert(add);
    }
    
    for (int x : recurring)
        cout << x << "  ";
    cout << endl;

    return EXIT_SUCCESS;
}
