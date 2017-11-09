#include <iostream>


using namespace std;

class Base {
public:
    int i;
    virtual void Print() { cout << "Base:Print" ; }
};


class Derived : public Base{
public:
    int n;
    virtual void Print() { cout <<"Drived:Print" << endl; }
};


int main() {
    Derived d;
    cout << sizeof( Base) << ","<< sizeof( Derived ) ;
    return 0;
}
