#include "Subscriber.h"
/*
inline map<string, string> set_address(string city, string street, string house)
{
    map<string, string> address = {{"city", city}, {"street" , street}, {"house", house}};
    return address;
}
*/

unsigned long Subscriber::get_number()
{
    return m_number;
}

string Subscriber::get_name()
{
    return m_name;
}

map<string, string> Subscriber::get_address()
{
    return m_address;
}
