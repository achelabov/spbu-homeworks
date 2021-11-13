struct BNode
{
    int data;
    BNode *left, *right;
    BNode(int d, BNode *l = nullptr, BNode *r = nullptr) :
        data(d), left(l), right(r) {}
};

class BTree
{
private:
    BNode *root;

public:
    BTree(BNode *p = nullptr) : root(p) {}
    void print();
    void fill_tree();
    BNode* get_left_node();
    void rm_left_node();
    void add_left_node(int data);
    BNode* get_left_leaf();
    void rm_left_leaf();
};
