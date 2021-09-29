struct DNode
{
    int data;
    DNode* next;
    DNode* prev;

    DNode(int d = 0, DNode* n = nullptr, DNode* p = nullptr) :
       data(d), next(n), prev(p) {} 
};

class DList
{
private:
    DNode* head;
    DNode* tail;
    
public:
    DList();
    ~DList();

    void add_first(int d);
    void print();
    void print_reverse();
    int length();
    DNode* last();
    DNode* prelast();
    void add_after_first(int d);
    void add_last(int d);
    void insertp(int d, int index);
    void delp(int index);
    void del_first();
    void del_second();
    void del_last();
    void del();
};
