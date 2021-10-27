#include "DataBase.h"

void DataBase::add_subscriber(unsigned long number, string name,
       string city, string street, string house)
{
    map<string, string> address = {{"city", city}, 
                                   {"street", street}, 
                                   {"house", house}};
    Subscriber sub(number, name, address);
    base.push_back(sub);
}

void DataBase::delete_subscriber(unsigned long number)
{
    for (auto it = base.begin(); it != base.end();)
    {
        if (it->get_number() == number)
            it = base.erase(it);
        else 
            ++it;
    }
}

void DataBase::print_data(unsigned long number)
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
    in >> it.get_number() >> it.get_name() 
        >> it.get_address()["city"] 
        >> it.get_address()["street"]
        >> it.get_address()["house"];

    return in;
}*/
