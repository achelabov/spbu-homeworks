#include "BTree.h"
#include <iostream>
using namespace std;

int main()
{
    BTree tree;
    tree.fill_tree();
    tree.print();
    cout << endl;
//    tree.scale();
//    tree.print();
    cout << tree.sum() << endl;
    cout << tree.count_neg() << endl;
    cout << tree.height() << endl;
    cout << tree.mult() << endl;
//    tree.reflect();
//    tree.print();
//    cout << tree.find(1) << endl;
    cout << tree.min() << endl;
    return 0;
}
