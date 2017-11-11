#include<iostream>
#include<typeinfo>

using namespace std;

int main()
{
	int i=3, *p = &i;
	char c = 'b';
	float x = 2.14, *q=&x;
	cout << "i+c: " << i+c <<"  type: " <<typeid(i+c).name() << endl;
	cout << "x+i: " << x+i <<"  type: " << typeid(x+i).name() << endl;
	cout << "p+i: " << p+i <<"  type: " << typeid(p+i).name() << endl;
	cout << "p==&i: " << (p==&i) <<"  type: " << (typeid(p==&i).name()) << endl;
	cout << "*p-*q: " << i+c <<"  type: " << typeid(*p-*q).name() << endl;
	cout << "static_cast<int>(x+i): " << (static_cast<int>(x+i)) <<"  type: " << typeid(static_cast<int>(x+i)).name() << endl;

}
