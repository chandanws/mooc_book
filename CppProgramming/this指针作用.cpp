// this指针作用

#include <iostream>
using namespace std;

class A
{
private:
    int i;
public:
    void Hello() { cout << "hello" << endl; }
};

//this若为NULL，则出错！！
int main()
{
    A *p = NULL;
    p->Hello();
}
