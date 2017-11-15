#include <iostream>
using namespace std;


class CBase {
public:
    virtual void SomeVirtualFunction() { }
};

class CDerived:public CBase {
public:
    virtual void SomeVirtualFunction() { }
};

int main() {
    CDerived ODerived;
    
    CBase *p = &ODerived;
    p->SomeVirtualFunction(); //调用哪个虚函数取决于p指向哪种类型的对象
    
    CBase & r = ODerived;
    r.SomeVirtualFunction(); //调用哪个虚函数取决于r引用哪种类型的对象
    
    return 0;
}
