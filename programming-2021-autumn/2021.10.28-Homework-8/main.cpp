#include "BTree.h"
#include <iostream>
using namespace std;

int main()
{
    BTree tree;
    tree.fill_tree();
//    tree.add_left_node(54);
//    tree.rm_left_node();
    tree.rm_left_leaf();
    tree.print();
    cout << endl;
    cout << tree.get_left_node()->data << endl;
//    cout << tree.get_left_leaf()->data << endl;
    return 0;
}
