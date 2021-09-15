#include "list.h"

int main()
{
    List list;
    list.add_first(1);
    list.add_first(2);
    list.add_first(3);
    list.add_first(4);
    list.add_first(5);

    list.add_after_first(90);
    list.add_last(228);
    list.del_last();
    
    list.insertp(1337, 2);

    list.print();

    return 0;
}
