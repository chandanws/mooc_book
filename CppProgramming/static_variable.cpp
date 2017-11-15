#include <iostream>

using namespace std;

class MyClass{
public:
	int n;
    static void PrintTotal(){cout << "yes" <<endl;};
    static int s;
};


int MyClass:: s = 0;
int main(){
	MyClass a, b;
    MyClass *p = &a;
	cout << sizeof(MyClass) << endl;


    MyClass::PrintTotal();
    a.PrintTotal();
    p->PrintTotal();
    cout << a.s << endl;
    a.s = 10;
    cout << b.s << endl;
}
