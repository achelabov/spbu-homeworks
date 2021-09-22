struct Node
{
    int data;
    Node* next;

    Node(int d = 0, Node* n = nullptr) : data(d), next(n) {}
};

struct List
{
    Node* head;
    List();
    ~List();
    List(const List& l);
    List& operator=(const List& l);

    void add_first(int d);
    void print();
    int length();
    Node* last();
    Node* prelast();
    Node* get_ptr(int n);
    void add_after_first(int d);
    void add_last(int d);
    void del_last();
    void del_first();
    void insertp(int d, int index);
    void delp(int index);
    void del();
};
