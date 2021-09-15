#include "list.h"
#include <iostream>

List::List()
{
    head = nullptr;
}

void List::add_first(int d)
{
    Node* tmp;
    tmp = new Node(d, head);
    head = tmp;
}

int List::length()
{
    Node* c_node = head;

    int i = 0;
    while (c_node != nullptr)
    {
        ++i;
        c_node = c_node->next;
    }

    return i;
}

Node* List::last()
{
    Node* c_node = head;

    for (int i = 0; i < length() - 1; ++i)
    {
        c_node = c_node->next;
    }

    return c_node;
}

Node* List::prelast()
{
    Node* c_node = head;

    for (int i = 0; i < length() - 2; ++i)
    {
        c_node = c_node->next;
    }

    return c_node;
}

Node* List::get_ptr(int n)
{
    Node* c_node = head;

    for (int i = 0; i < length() - n - 1; ++i)
    {
        c_node = c_node->next;
    }

    return c_node;
}

void List::add_after_first(int d)
{
    Node* c_node = new Node(d, head->next);
    head->next = c_node;
}

void List::add_last(int d)
{
    Node* c_node = new Node(d, nullptr);
    Node* last = head;
    for (int i = 0; i < length() - 1; ++i)
    {
        last = last->next;
    }
    last->next = c_node;
}

void List::del_last()
{
    Node* prelast = head;
    for (int i = 0; i < length() - 2; ++i)
    {
        prelast = prelast->next;
    }
    delete prelast->next->next;
    prelast->next = nullptr;
}

void List::insertp(int d, int index)
{
    if (index == 0)
    {
        add_first(d);
    }
    else if (index == 1)
    {
        add_after_first(d);
    }
    else if (index == length() - 1)
    {
        add_last(d);
    }
    else
    {
        Node* prev_node = head;
        for (int i = 0; i < index - 1; ++i)
        {
            prev_node = prev_node->next;
        }
        Node* c_node = new Node(d, prev_node->next);
        prev_node->next = c_node;
    }
}

/*
void List::delp(int index)
{
    if (index == 0)
    {
        Node* c_node = head;
        head = head->next;
        delete c_node;
    }
    else if (index == length() - 1)
    {
        del_last();
    }
    else
    {
        Node* prev_node = head;
        for (int i = 0; i < index - 2; ++i)
        {
            prev_node = prev_node->next;
        }
        prev_node->next->next = prev_node;
        delete prev_node->next;
    }
}
*/

void List::print()
{
    Node* c_node = head;

    while (c_node != nullptr)
    {
        std::cout << c_node->data << " ";
        c_node = c_node->next;
    }
}
