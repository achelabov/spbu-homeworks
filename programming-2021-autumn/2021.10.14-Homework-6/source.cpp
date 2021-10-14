#include <iostream>
#include <string>
#include <algorithm>
#include <stack>
#include <vector>
#include <map>

using namespace std;

inline bool space(char c)
{
    return isspace(c);
}

inline bool notspace(char c)
{
    return !isspace(c);
}

vector<string> split(const string& s)
{
    vector<string> ret;
    string::const_iterator iter = s.begin();

    while (iter != s.end())
    {
        iter = find_if(iter, s.end(), notspace);
        string::const_iterator j = find_if(iter, s.end(), space);
        if (iter != s.end())
        {
            ret.push_back(string(iter, j)); 
            iter = j;
        }
    }

    return ret;
}

bool is_digit(const string& s)
{
    string::const_iterator iter = s.begin();
    while (iter != s.end() && ::isdigit(*iter)) ++iter;

    return !s.empty() && iter == s.end();
}

bool is_sign(const string& s)
{
    return s == "+" || s == "-" || s == "*" || s == "/";
}

int str_to_int(const string& s)
{
    return std::stoi(s);
}

int use_sign(int sign, int f_num, int s_num)
{
    switch (sign)
    {
        case 0: return f_num + s_num;
        case 1: return f_num - s_num;
        case 2: return f_num * s_num;
        case 3: return s_num ? f_num / s_num : -1;
    }
    return -1;
}

int define_sign(string sign)
{
    map<string, int> display = {{"+", 0}, {"-", 1}, 
                                {"*", 2}, {"/", 3}};
    return display[sign];
}

int reverse_polish_notation()
{
    string str = "3 4 * 2 +";
//    cin >> str;
    stack<int> rpn_stack;

    vector<string> str_arr = split(str);

    for (int i = 0; i < str_arr.size(); ++i)
    {
        if (is_digit(str_arr[i]))
        {
            rpn_stack.push(str_to_int(str_arr[i]));
        }
        else if (is_sign(str_arr[i]))
        {
            int f_num = rpn_stack.top();
            rpn_stack.pop();
            int s_num = rpn_stack.top(); 
            rpn_stack.pop();
            rpn_stack.push(use_sign(define_sign(str_arr[i]), f_num, s_num));
        }
        else
        {
            return -1;
        }
    }
    return rpn_stack.top();
}

int main()
{
      cout << reverse_polish_notation() << endl;
/*    string str = "22 33 + 11 55 -";
    string str;
    cin >> str;    
    vector<string> vect = split(str);
    
    for (int i = 0; i < vect.size(); ++i)
    {
        cout << vect[i] << endl;
    }
*/
    return 0;
}
