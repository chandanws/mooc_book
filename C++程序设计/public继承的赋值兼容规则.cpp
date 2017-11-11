#include <iostream>
using namespace std;


class base { };
class derived : public base { };

int main()
{
    base b; derived d;
    
    //派生类的对象可以赋值给基类对象
    b = d;
    
    //派生类对象可以初始化基类引用
    base &br = d;
    
    //派生类对象的地址可以赋值给基类指针
    base *pb = &d;
}
