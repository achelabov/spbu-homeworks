#include "DList.h"
#include <iostream>
int main()
{
    DList list;
    list.add_first(3);
    list.add_first(2);
    list.add_first(1);
    list.add_last(4);
    list.add_last(5);
    list.add_last(6);
    list.add_last(7);
    list.add_after_first(889);
    list.del_first();
    list.del_last();
    list.insertp(213, 2);
    list.del_second(); 
    list.delp(3);
    list.print();
    list.print_reverse();
    
    std::cout << list.length() << std::endl;

    std::cout << list.prelast() << std::endl;
    std::cout << list.last() << std::endl;

    DList list2;
    list2 = list;

    list2.print();
    list2.print_reverse();
    
    return 0;
}
