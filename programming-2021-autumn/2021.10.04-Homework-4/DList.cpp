#include "DList.h"
#include <iostream>

DList::DList()
{
    head = nullptr;
    tail = nullptr;
}

DList::~DList()
{
    del();
}

DNode* copy(DNode* x)
{
    if (x == nullptr)
    {
        return nullptr;
    }
    DNode* y = new DNode(x->data, copy(x->next), nullptr);
    if (y->next != nullptr)
    {
        y->next->prev = y;
    }

    return y;
}

DList::DList(const DList& l)
{
    head = copy(l.head);
    tail = last();
}

DList& DList::operator=(const DList& l)
{
    del();
    head = copy(l.head);
    tail = last();

    return *this;
}

void DList::add_first(int d)
{
    DNode* new_node = new DNode(d, head, nullptr);

    if (head == nullptr)
    {
        tail = new_node;
    }
    else
    {
        head->prev = new_node;
    }
    head = new_node;
}

void DList::add_after_first(int d)
{
    DNode* it = head->next;
    DNode* new_node = new DNode(d, head->next);
    it->prev = new_node;
    new_node->prev = head;
    head->next = new_node;
}

void DList::add_last(int d)
{
    DNode* new_node = new DNode(d, nullptr, tail);
    tail->next = new_node;
    tail = new_node;
}

void DList::insertp(int d, int index)
{
    if (index == 0)
    {
        add_first(d);
    }
    if (index == 1)
    {
        add_after_first(d);
    }
    if (index == length())
    {
        add_last(d);
    }
    else
    {
        DNode* it = head;
        for (int i = 0; i < index - 1; ++i)
        {
            it = it->next;
        }
        DNode* tmp = it->next;
        DNode* new_node = new DNode(d, tmp, it);

        tmp->prev = new_node;
        it->next = new_node;

    }
}

void DList::del_first()
{
    DNode* del_node = head;
    head = head->next;
    head->prev = nullptr;
    delete del_node;
}

void DList::del_second()
{
    DNode* del_node = head->next;
    DNode* it = del_node->next;
    it->prev = head;
    head->next = it;
    delete del_node;
}

void DList::del_last()
{
    DNode* del_node = tail;
    tail = tail->prev;
    tail->next = nullptr;
    delete del_node;
}

void DList::delp(int index)
{
    if (index == 0)
    {
        del_first();
    }
    if (index == 1)
    {
        del_second();
    }
    if (index = length() - 1)
    {
        del_last();
    }
    else
    {
        DNode* it = head;
        for (int i = 0; i < index - 1; ++i)
        {
            it = it->next;
        }
        DNode* tmp = it->next;
        DNode* tmp2 = tmp->next;
        it->next = tmp2;
        tmp2->prev = it;
        delete tmp; 
    }
}

void DList::del()
{
    while (length())
    {
        del_first();
    }
}

int DList::length()
{
    DNode* c_node = head;
    int i = 0;

    while (c_node != nullptr)
    {
        ++i;
        c_node = c_node->next;
    }

    return i;
}

DNode* DList::last()
{
    return tail;
}

DNode* DList::prelast()
{
    return tail->prev;
}

void DList::print()
{
    DNode* c_node = head;

    while (c_node != nullptr)
    {
        std::cout << c_node->data << "  ";
        c_node = c_node->next;
    }

    std::cout << std::endl;
}

void DList::print_reverse()
{
    DNode* c_node = tail;

    while (c_node != nullptr)
    {
        std::cout << c_node->data << "  ";
        c_node = c_node->prev;
    }

    std::cout << std::endl;
}
