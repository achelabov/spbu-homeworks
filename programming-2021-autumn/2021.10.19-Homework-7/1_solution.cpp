#include <iostream>
#include <vector>

using namespace std;

template <typename T>
void enlarge(vector<T>& vect)
{
    for (auto i = vect.begin(); i != vect.end() - 1; ++i)
    {
        i = vect.insert(i, (*(i) + *(++i)) / 2);
    }
}

template <typename T>
void del(vector<T>& vect)
{
    for (auto i = vect.begin(); i != vect.end() - 1; ++i)
    {
        i = vect.erase(i);
    }
    vect.pop_back();
}

int main()
{
    vector<int> vect = {1, 3, 5, 8, 22, 34, 20};
    enlarge(vect);
    del(vect);

    for (int i = 0; i < vect.size(); ++i)
    {
        cout << vect[i] << endl;
    }

    return EXIT_SUCCESS;
}
