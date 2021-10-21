#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

template <typename T>
vector<T> concat(vector<T> f_vect, vector<T> s_vect)
{
    vector<T> vect;
    vect.resize(f_vect.size() + s_vect.size());
    copy(f_vect.begin(), f_vect.end(), vect.begin());
    copy(s_vect.begin(), s_vect.end(), vect.begin() + f_vect.size());

    return vect;
}

template <typename T>
vector<T> repeat(vector<T> vect, unsigned n)
{
    vector<T> s_vect = vect;

    for (int i = 0; i < n; ++i)
    {
        vect = concat(vect, s_vect);
    }

    return vect;
}

int main()
{
    vector<int> vect = {1, 2, 3, 4, 5, 6};
    int* arr = new int[vect.size()];

    copy(vect.begin(), vect.end(), arr);
 
    for (int i = 0; i < vect.size(); ++i)
    {
        cout << arr[i] << " ";
    }
    cout << endl;

    vector<int> vect2 = concat(vect, vect);

    for (auto i : vect2)
    {
        cout << i << " ";
    }
    cout << endl;

    vector<int> vect3 = repeat(vect, 4);

    for (auto i : vect3)
    {
        cout << i << " ";
    }
    cout << endl;

    return EXIT_SUCCESS;
}
