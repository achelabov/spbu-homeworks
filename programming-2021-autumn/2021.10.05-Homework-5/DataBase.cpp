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
    }

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
    
    friend ostream& operator<< (ostream& out, DataBase& db);
    friend istream& operator>> (istream& in, const DataBase& db);
};

ostream& operator<< (ostream& out, DataBase& db)
{
//    out << db.base.begin()->get_name();
    for (auto& it : db.base)
    {
        out << it.get_number() << '\t' << it.get_name() << '\t' 
            << it.get_address()["city"] 
            << '\t' << it.get_address()["street"] << '\t' 
            << it.get_address()["house"] << '\t';
    }
    
    return out;
}
/*
istream& operator>> (istream& in, const DataBase& db)
{
    in >>
    return in;
}*/
