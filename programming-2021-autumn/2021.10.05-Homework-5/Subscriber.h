#include <string>
#include <map>

using namespace std;

class Subscriber
{
private:
    unsigned long m_number;
    string m_name;
    map<string, string> m_address;

public:
    Subscriber(unsigned long number, string name, map<string, string> address):
        m_number(number),  m_name(name), m_address(address) {};
    
    unsigned long get_number();
    string get_name();
    map<string, string> get_address();
//  map<string, string> set_address(string city, string street, string house);
};
