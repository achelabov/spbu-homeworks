#include "BTree.h"
#include <iostream>

using namespace std;

void f_print(BNode *root, int d = 0)
{
    if (root == nullptr) return;
    f_print(root->right, d + 3);
    for (int i = 0; i < d; ++i)
        cout << ' ';
    cout << root->data << endl;
    f_print(root->left, d + 3);
}

void BTree::print()
{
    f_print(root);
}

BNode* first_solution()
{
    BNode *p13 = new BNode(13),
          *p7 = new BNode(-7),
          *p4 = new BNode(4),
          *p1 = new BNode(1),
          *p14 = new BNode(-14, p13),
          *p6 = new BNode(6, p4, p7),
          *p10 = new BNode(10, nullptr, p14),
          *p3 = new BNode(-3, p1, p6),
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

void treversal_mthree(BNode* root)
{
    if (root == nullptr)
    {
        return;
    }
    root->data = root->data * 3;
    treversal_mthree(root->left);
    treversal_mthree(root->right);
}

void BTree::scale()
{
    treversal_mthree(root);
}

int treversal_sum(BNode* root)
{
    if (root == nullptr)
    {
        return 0;
    }
    return root->data + treversal_sum(root->left) + treversal_sum(root->right);
}

int BTree::sum()
{
    return treversal_sum(root);
}

int treversal_neg(BNode* root)
{
    if (root == nullptr)
    {
        return 0;
    }
    return (root->data < 0 ? 1 : 0) + treversal_neg(root->left) +  treversal_neg(root->right);
}

int BTree::count_neg()
{
    return treversal_neg(root);
}

int treversal_height(BNode* root)
{
    if (root == nullptr)
    {
        return 0;
    }
    return 1 + (treversal_height(root->left) > treversal_height(root->right) ?
                treversal_height(root->left) : treversal_height(root->right));
}

int BTree::height()
{
    return treversal_height(root);
}

void treversal_reflect(BNode* root)
{
    if (root == nullptr)
    {
        return;
    }
    BNode* tmp = root->left;
    root->left = root->right;
    root->right = tmp;
    treversal_reflect(root->left);
    treversal_reflect(root->right);
}

void BTree::reflect()
{
    treversal_reflect(root);
}

int treversal_pmult(BNode* root)
{
    if (root == nullptr)
    {
        return 1;
    }
    return (root->left != nullptr && root->right != nullptr ? 
            root->left->data * root->right->data : 1)
            * treversal_pmult(root->left) * treversal_pmult(root->right);
}

int BTree::mult()
{
    return treversal_pmult(root);
}

template <class T>
BNode* treversal_find(T d, BNode* root)
{
    if (root == nullptr)
    {
        return root;
    }
    return root->data == d ? root : [=](){treversal_find(d, root->left);
                                          treversal_find(d, root->right);};
}

template <class T>
BNode* BTree::find(T d)
{
    return treversal_find(d, root);
}

int treversal_min(int d, BNode* root)
{
    if (root == nullptr)
    {
        return d;
    }
    if (d > root->data)
    {
        d = root->data;
    }
    return treversal_min(d, root->left) < treversal_min(d, root->right) ?
           treversal_min(d, root->left) : treversal_min(d, root->right);
}

int BTree::min()
{
    return treversal_min(root->data, root);
}
