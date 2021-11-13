#include "BTree.h"
#include <iostream>

using namespace std;

void f_print(BNode *root, int d = 0)
{
    if (root == nullptr) return;
    f_print(root->right, d + 3);
    for (int i = 0; i < d; ++i)
        cout << ' ';
    cout << root->data << "( " << root->left << " | " << root->right << " | " << root << " )  " << endl;
    f_print(root->left, d + 3);
}

void BTree::print()
{
    f_print(root);
}

BNode* first_solution()
{
    BNode *p13 = new BNode(13),
          *p7 = new BNode(7),
          *p4 = new BNode(4),
          *p1 = new BNode(1),
          *p14 = new BNode(14, p13),
          *p6 = new BNode(6, p4, p7),
          *p10 = new BNode(10, nullptr, p14),
          *p3 = new BNode(3, p1, p6),
          *p8 = new BNode(8, p3, p10);
    return p8;
}

void BTree::fill_tree()
{
    root = first_solution();
}

BNode* left_node(BNode *root)
{
    if (root->left == nullptr) return root;
    return left_node(root->left);
}

BNode* BTree::get_left_node()
{
    return left_node(root);
}

void BTree::rm_left_node()
{
    BNode *c_node = root;
    BNode *del_node = nullptr;
    while (c_node->left->left != nullptr)
    {
        c_node = c_node->left;
    }
    del_node = c_node->left;
    c_node->left = c_node->left->right;
    delete del_node;
}

void BTree::add_left_node(int data)
{
    BNode *new_node = new BNode(data);
    get_left_node()->left = new_node;
}

BNode* left_leaf(BNode *root)
{
    if (root->left == nullptr && root->right == nullptr)
    {
        return root;
    }
    return left_leaf(root->left);
    if (root->left == nullptr && root->right != nullptr)
    {
        return left_leaf(root->right);
    }
}

BNode* BTree::get_left_leaf()
{
    return left_leaf(root);
}

void BTree::rm_left_leaf()
{
    BNode* c_node = root;
    BNode* p_node = nullptr;
    while (c_node->left != nullptr || c_node->right != nullptr)
    {
        if (c_node->left != nullptr)
        {
            p_node = c_node;
            c_node = c_node->left;
        } else
        {
            p_node = c_node;
            c_node = c_node->right;
        }
    }
    delete c_node;
    if (p_node->left != nullptr)
    {
        p_node->left = nullptr;
    } else
    {
        p_node->right = nullptr;
    }
}
