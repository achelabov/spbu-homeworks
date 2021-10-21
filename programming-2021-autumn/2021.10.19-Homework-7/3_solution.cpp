#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int>::iterator second_entry(vector<int> vect, int value)
{
    int count = 0;
    return find_if(vect.begin(), vect.end(), 
                  [&count, value] (int c_it) 
                  {
                    if (c_it == value) ++count;
                    return (count == 2); 
                  });
}

vector<int>::iterator last_entry(vector<int> vect, int value)
{
    reverse(vect.begin(), vect.end());
    return vect.end() - find(vect.begin(), vect.end(), value);
}

bool subseq(vector<int> vect, vector<int> sub)
{
    auto s_it = vect.begin();
	for (auto i = sub.begin(); i != sub.end(); i++)
	{
		s_it = find(s_it, vect.end(), *i);
		if (s_it == vect.end())
		{
			return false;
		}
		s_it++;
	}
	return true;
}

int main()
{
    vector<int> vect = {12, 92, 44, 2, 3, 92, 5};

    cout << *second_entry(vect, 92) << endl;

    cout << *last_entry(vect, 92) << endl;
    return EXIT_SUCCESS;
}
