#include "Subscriber.h"
#include <iostream>
#include <list>

class DataBase
{
private:
    list<Subscriber> base;

public:
    void add_subscriber(unsigned long number, string name,
           string city, string street, string house)
    {
        map<string, string> address = {{"city", city}, 
                                       {"street", street}, 
                                       {"house", house}};
        Subscriber sub(number, name, address);
        base.push_back(sub);
    }

    void delete_subscriber(unsigned long number)
    {
        for (auto it = base.begin(); it != base.end();)
        {
            if (it->get_number() == number)
                it = base.erase(it);
            else 
                ++it;
        }
/*        for (auto& it : base)
        {
            if (it.get_number() == number)
            {
                base.erase(it);
            }
        }
*/    }

    void print_data(unsigned long number)
    {
        for (auto& it : base)
        {
            if (it.get_number() == number)
            {
                cout << "Name: " << it.get_name() << "\t";
                cout << "City: " << it.get_address()["city"] << "\t";
                cout << "Street: " << it.get_address()["street"] << "\t";
                cout << "House: " << it.get_address()["house"] << "\t";
                cout << endl;
            }
        }
    }
};
