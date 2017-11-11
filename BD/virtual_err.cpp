#include <iostream>

using namespace std;

class Base {
	public:
		virtual void foo(int i)
		{cout << "Base:: i = " << i << endl;}
		virtual void foo(double x)
		{cout << "Base:: x= " << x << endl;}
};

class Derived: public Base
{
	public:
		void foo(int i)
		{cout << "Derived:: i = " << i << endl;}
};

class Derived2: public Derived
{
	public:
		void foo(int i)
		{cout << "Derived2::i= " << i << endl;}
		void foo(double d)
		{cout << "Derived2::d= " << d << endl;}
};

int main()
{
	Derived d;
	Derived2 d2;
	Base b, *pb = &d;

	b.foo(9); // selects Base::foo(int);
	b.foo(9.5); //selects Base::foo(double);
	d.foo(9); // selects Derived::foo(int);
	d.foo(9.5); //selects Derived:foo(int);
	pb -> foo(9); //selects Derived::foo(int);
	pb -> foo(9.5); //selects Base:: foo(double);
	pb = & d2;
	pb -> foo(9); //selects Derived2:;foo(int);
	pb -> foo(9.5); //selects Derived2::foo(double)
}


