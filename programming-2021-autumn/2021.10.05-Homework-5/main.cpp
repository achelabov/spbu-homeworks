#include "DataBase.cpp"

int main()
{
    DataBase base;
    base.add_subscriber(1, "Name1", "123", "2321", "113");
    base.add_subscriber(2, "Name2", "123", "2321", "113");
    base.add_subscriber(3, "Name3", "123", "2321", "113");

    base.print_data(1);
    base.print_data(2);
    base.print_data(3);
    
    base.delete_subscriber(2);
    cout << endl;

    base.print_data(1);
    base.print_data(3);

//    cout << base;
    return 0;
}
