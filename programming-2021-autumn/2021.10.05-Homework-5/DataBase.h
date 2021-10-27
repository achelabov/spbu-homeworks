#include "Subscriber.h"
#include <iostream>
#include <list>

class DataBase
{
private:
    list<Subscriber> base;

pubic:
    void add_subscriber(unsigned long number, string name,
            string city, string street, string house);
    void delete_subscriber(unsigned long number);
    void print_data(unsigned long number);
    friend ostream& operator<< (ostream& out, DataBase& db);
    friend istream& operator>> (istream& in, DataBase& db);
};

